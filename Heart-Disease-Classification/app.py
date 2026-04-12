from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import requests

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, 'models', 'heart_model.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR, 'models', 'scaler.pkl'), 'rb'))

def fetch_air_quality():
    try:
        url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=40.71&longitude=-74.00&current=pm2_5"
        response = requests.get(url, timeout=3).json()
        pm25 = response['current']['pm2_5']
        risk = "High" if pm25 > 35 else "Moderate" if pm25 > 12 else "Low"
        return {"pm25": pm25, "risk": risk}
    except:
        return {"pm25": "--", "risk": "Unknown"}

def get_detailed_analysis(category_num, risk_level, age, chol, oldpeak, trestbps):
    analysis = {
        "category": f"Category {category_num}",
        "risk_level": risk_level,
        "color": "success" if category_num == 0 else "info" if category_num == 1 else "warning" if category_num == 2 else "danger",
        "tips": []
    }
    
    if category_num > 0:
        analysis["tips"].append(f"🚨 **Clinical Alert:** The model detected a {risk_level.lower()} of coronary artery disease. Please schedule a cardiology consult.")
        if oldpeak > 1.5:
            analysis["tips"].append("📉 **ECG Anomaly:** Your 'Oldpeak' (ST Depression) is elevated. This indicates your heart muscle may be deprived of oxygen during physical stress.")
    else:
        analysis["tips"].append("✅ **Positive Indicator:** Your metrics align tightly with the healthy patient clusters in our training dataset.")

    if chol > 240:
        analysis["tips"].append("🩸 **Lipid Profile:** Cholesterol is dangerously high (>240mg/dl). Immediate dietary changes (Mediterranean diet) and statin consultation recommended.")
    elif chol > 200:
        analysis["tips"].append("⚠️ **Lipid Profile:** Borderline high cholesterol. Increase dietary fiber and Omega-3 intake.")
        
    if trestbps > 130:
        analysis["tips"].append("🫀 **Blood Pressure:** Your resting BP is elevated. Consider monitoring your sodium intake and practicing stress-reduction techniques.")

    if age > 50 and category_num == 0:
        analysis["tips"].append("⏳ **Longevity:** As you are over 50, maintain 150 minutes of zone-2 cardio weekly to keep arterial walls flexible.")

    return analysis

@app.route('/')
def home():
    env_data = fetch_air_quality()
    return render_template('index.html', env=env_data)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        env_data = fetch_air_quality()

        # Capture Form Inputs
        age = float(request.form['age'])
        sex = request.form['sex'] 
        cp = request.form['cp']   
        chol = float(request.form['chol'])
        thalch = float(request.form['thalch'])
        trestbps = float(request.form['trestbps']) 
        oldpeak = float(request.form.get('oldpeak', 0.0)) 

        user_data = {
            "Age": int(age),
            "Biological Sex": sex,
            "Chest Pain Type": cp.title(),
            "Resting BP (mmHg)": int(trestbps),
            "Cholesterol (mg/dl)": int(chol),
            "Max Heart Rate": int(thalch),
            "ST Dep. (Oldpeak)": float(oldpeak)
        }

        # 1. SCALE CONTINUOUS FEATURES (5 features)
        cont_features = np.array([[age, trestbps, chol, thalch, oldpeak]])
        scaled_cont = scaler.transform(cont_features)
        
        # 2. CONSTRUCT 9-FEATURE VECTOR
        features = list(scaled_cont[0]) 
        dummies = [0] * 4 
        
        if sex == 'Male': dummies[0] = 1
        
        if cp == 'atypical angina': dummies[1] = 1
        elif cp == 'non-anginal': dummies[2] = 1
        elif cp == 'typical angina': dummies[3] = 1

        full_vector = np.array([features + dummies])

        # 3. PROBABILITY ENGINE: Map confidence to Category 0, 1, 2, 3
        probability = model.predict_proba(full_vector)[0][1] # Gets the % chance of disease

        if probability < 0.25:
            cat_num = 0
            risk_level = "Low Risk / Stable"
        elif probability < 0.50:
            cat_num = 1
            risk_level = "Mild Risk"
        elif probability < 0.75:
            cat_num = 2
            risk_level = "Moderate Risk"
        else:
            cat_num = 3
            risk_level = "High Risk"

        # Generate custom tips based on Category
        analysis = get_detailed_analysis(cat_num, risk_level, age, chol, oldpeak, trestbps)

        return render_template('index.html', 
                               category=analysis["category"], 
                               risk_level=analysis["risk_level"], 
                               alert_class=analysis["color"], 
                               tips=analysis["tips"],
                               env=env_data,
                               show_results=True,
                               user_data=user_data)

    except Exception as e:
        return render_template('index.html', error=f"System Error: {str(e)}", env=fetch_air_quality())

if __name__ == "__main__":
    app.run(debug=True)

app=app