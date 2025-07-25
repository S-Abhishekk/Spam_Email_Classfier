
<h1 align="center">🚀📧 Spam Email Classifier 🔍💌</h1>
<p align="center">
  <b>💼 Final Internship Project at Celebal Technologies 💼</b><br>
  <i>Machine Learning | Streamlit | Random Forest | Real-Time Spam Detection</i>
</p>

---

## 📚 Overview

Welcome to the **Spam Email Classifier** — a complete end-to-end ML project that classifies emails as **Spam** 🧨 or **Not Spam** 📬 using the famous UCI Spambase dataset.  
This is my final project for the **Data Science Internship at Celebal Technologies**. 💻🧠

---

## 🧠 What This Project Does

✨ **Detects spam emails using machine learning**  
⚡ Built with **Random Forest** classifier  
🌐 Clean, real-time interface powered by **Streamlit**  
📂 Uses preloaded `.data` file, so no need to upload anything manually  
📊 Simple, elegant, and ready to deploy

---

## 🎯 Features

- ✅ Real-time prediction: Enter data, get instant spam detection
- 🤖 ML Model trained on 4600+ emails
- 📊 No CSV uploads needed – loads from `spambase.data`
- 📈 >94% model accuracy
- 💻 Interactive web dashboard via Streamlit

---

## 🛠️ Tech Stack

| 🔧 Tool          | 💡 Usage                          |
|------------------|-----------------------------------|
| 🐍 Python        | Core Programming Language         |
| 📊 Pandas/NumPy  | Data Manipulation                 |
| 🤖 Scikit-Learn  | Model Training & Evaluation       |
| 💾 Joblib        | Saving Trained Model              |
| 🖼️ Streamlit     | Dashboard & Web App               |
| 🧪 Virtualenv    | Environment Management            |

---

## 📁 Project Structure

```bash
📦 Spam_Email_Classifier
├── app.py                 # 🎨 Streamlit frontend
├── train_model.py         # 🏋️ Model training script
├── spambase.data          # 🧾 Raw dataset
├── spam_classifier.pkl    # 💾 Trained model
├── requirements.txt       # 📦 Required packages
└── README.md              # 📘 You are here!
```

---

## 🚀 How to Run This Project (Step-by-Step)

### 1️⃣ Clone this repository
```bash
git clone https://github.com/S-Abhishekk/Spam_Email_Classfier
cd Spam_Email_Classifier
```

### 2️⃣ Create a virtual environment 🌱
```bash
python3 -m venv venv
source venv/bin/activate      # 🐧 For Linux/macOS/Codespaces
# OR
venv\Scripts\activate         # 🪟 For Windows
```

### 3️⃣ Install the dependencies 📦
```bash
pip install -r requirements.txt
```

### 4️⃣ Train the model (if not already trained) 🤖
```bash
python train_model.py
```

> This generates a file: `spam_classifier.pkl` which is used by the Streamlit app

### 5️⃣ Launch the Streamlit web app 🚪
```bash
streamlit run app.py
```

Then open your browser to:
```
http://localhost:8501
```

