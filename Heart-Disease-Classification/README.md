# ❤️ HeartHealth AI | Clinical Neural Diagnostics

![Vercel Deployment](https://img.shields.io/badge/Vercel-Deployed-success?style=for-the-badge&logo=vercel)
![Python Version](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Framework](https://img.shields.io/badge/Flask-v3.0-red?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**HeartHealth AI** is a high-fidelity web application leveraging **Logistic Regression** and **Explainable AI (XAI)** to provide clinical-grade cardiovascular risk assessments. 

---

## 🌐 Live Deployment
**Experience the live dashboard here:** 🚀 **[LIVE DEMO LINK](https://heart-disease-classification-hm0y234zd-kamilperwezs-projects.vercel.app/)**

---

## 📸 Project Gallery

| Neural Diagnostic Dashboard | 3D Anatomy Visualization |
| :---: | :---: |
| ![Dashboard Screenshot 1](https://github.com/kamilperwez/Heart-Disease-Classification/blob/main/static/main.png?raw=true) | ![3D Heart Screenshot 2](https://github.com/kamilperwez/Heart-Disease-Classification/blob/main/static/heart.png?raw=true) |

| Live Risk Analysis & XAI |
| :---: |
| ![Risk Analysis 3](https://github.com/kamilperwez/Heart-Disease-Classification/blob/main/static/dash.png?raw=true) |

---

## 🚀 Key Features

* **Neural Diagnostics:** Real-time risk classification (Low to High) using an optimized Logistic Regression pipeline.
* **Explainable AI (XAI):** A custom **Feature Impact Analysis** engine visualizing which biological factors (Age, Chol, BP) moved the needle.
* **3D Clinical Anatomy:** Native WebGL rendering of the heart using Google’s `model-viewer`.
* **Live Environmental Risk:** Open-Meteo API integration tracking atmospheric PM2.5 levels.
* **Holographic UI:** "Medical Terminal" aesthetic with glassmorphism and live EKG pulse animations.

---

## 🛠️ Technical Stack

<p align="left">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white" />
  <img src="https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white" />
</p>

---

## 📂 Directory Structure

```text
/
├── app.py              # Main Flask Entry Point (Root)
├── models/             # Pickled ML Model & Scaler
├── static/             # 3D GLB Models & Image Assets
├── templates/          # Glassmorphic UI (HTML)
├── vercel.json         # Deployment Configuration
└── requirements.txt    # Serverless Dependencies
