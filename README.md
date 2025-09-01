# 🤖 DocBot AI - A Medicine Recommendation Bot!  

**DocBot AI** is an intelligent healthcare assistant built with **Machine Learning** and **Streamlit**.  
It predicts possible **diseases based on user symptoms** and provides detailed recommendations such as **precautions, medications, diets, and workouts**.  

---

## 📑 Table of Contents  

- [📖 Introduction](#-introduction)  
- [✨ Features](#-features)  
- [📂 Dataset](#-dataset)  
- [🚀 Installation](#-installation)  
- [⚙️ Setup](#️-setup)  
- [🖥️ Usage](#️-usage)  
- [🛠️ Tech Stack](#-tech-stack)  
- [📌 Requirements](#-requirements)  
- [🏗️ Project Structure](#️-project-structure)  
- [📄 License](#-license)  
- [🤝 Contributing](#-contributing)  
- [🙌 Acknowledgments](#-acknowledgments)  
- [📧 Contact](#-contact)  

---

## 📖 Introduction  

Healthcare often begins with **early diagnosis**. Patients describe symptoms, and doctors predict possible illnesses.  

**DocBot AI** replicates this process using **machine learning models** trained on medical datasets.  
It acts as a **virtual health assistant** by:  

- Taking user symptoms as input  
- Predicting the most probable disease  
- Suggesting precautions, medications, diets, and workouts  

⚠️ **Disclaimer**: This tool is **not a replacement for professional medical advice**. Always consult a licensed doctor for accurate diagnosis and treatment.  

---

## ✨ Features  

- 🩺 **Disease Prediction** → Input symptoms, get predicted disease.  
- 💊 **Medication Suggestions** → Lists possible medicines.  
- 🥦 **Diet Recommendations** → Suggests foods to improve health.  
- 🧘 **Workout Guidance** → Suggests light exercises for recovery.  
- 🛡️ **Precautionary Measures** → Provides preventive steps to follow.  
- 📖 **Disease Descriptions** → Easy-to-understand explanation of the disease.  

---

## 📂 Dataset  

DocBot AI uses multiple CSV files to store medical knowledge:  

- `description.csv` → Descriptions of diseases  
- `diets.csv` → Recommended diets for each disease  
- `medications.csv` → Possible medications  
- `precautions_df.csv` → Precautionary measures  
- `symtoms_df.csv` → Symptoms dataset  
- `Symptom-severity.csv` → Symptom severity mapping  
- `workout_df.csv` → Suggested workouts  
- `Training.csv` → Training dataset for model  

---

## 🚀 Installation  

Clone the repo and install dependencies:  

```bash
git clone https://github.com/Mohd-Muzammil7052/Medicine_Recommendation_Model_With_Disease_Details_ML_Model.git
cd Medicine_Recommendation_Model_With_Disease_Details_ML_Model
pip install -r requirements.txt
```

## ⚙️ Setup

1. Ensure all CSV files (description.csv, diets.csv, medications.csv, etc.) are placed in the project root.

2. Ensure the trained model files model_svc.pkl and encoder.pkl are present in the root directory.

3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the Streamlit app in your browser.
2. Enter your symptoms (comma-separated). Example:
   ```text
   cough, fever, headache
   ```
3. Click Predict.
4. Get:
 * ✅ Predicted disease
 * 📖 Description
 * 💊 Medications
 * 🛡️ Precautions
 * 🥦 Diet plan
 * 🧘 Workout suggestions

---

## 🛠️ Tech Stack

* Streamlit → Web UI for chatbot.
- Scikit-learn → ML model training & prediction
+ Pandas & NumPy → Data handling
* Matplotlib & Seaborn → Data visualization

---

## 📌 Requirements

See [requirements.txt](https://github.com/Mohd-Muzammil7052/Medicine_Recommendation_Model_With_Disease_Details_ML_Model/blob/main/requirements.txt) for all dependencies:

```text
numpy
pandas
scikit-learn
matplotlib
seaborn
streamlit
```

---

## 🏗️ Project Structure  

```text
📦 DocBot-AI
 ┣ 📜 README.md            # Documentation
 ┣ 📜 app.py               # Streamlit app
 ┣ 📜 model.ipynb          # Notebook for training
 ┣ 📜 requirements.txt     # Dependencies
 ┣ 📜 model_svc.pkl        # Trained ML model
 ┣ 📜 encoder.pkl          # Label encoder
 ┣ 📜 description.csv      # Disease descriptions
 ┣ 📜 diets.csv            # Diet recommendations
 ┣ 📜 medications.csv      # Medications
 ┣ 📜 precautions_df.csv   # Precautionary steps
 ┣ 📜 symtoms_df.csv       # Symptoms dataset
 ┣ 📜 Symptom-severity.csv # Symptom severity mapping
 ┣ 📜 Training.csv         # Training dataset
 ┗ 📜 workout_df.csv       # Workout suggestions
```

---

## 📄 License  

This project is licensed under the [MIT License](https://opensource.org/license/mit).  
Feel free to use, modify, and distribute it as needed.

---

## 🤝 Contributing  

Contributions are welcome! 🎉  
If you’d like to improve this project:  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 🙌 Acknowledgments  

Special thanks to the amazing open-source tools powering this project:  

- [Scikit-Learn](https://scikit-learn.org/stable/)  
- [Pandas](https://pandas.pydata.org/)  
- [Numpy](https://numpy.org/)  
- [Streamlit](https://streamlit.io/)  

---

## 📧 Contact  

For queries or collaborations:  

**Mohd Muzammil**  
- [GitHub](https://github.com/Mohd-Muzammil7052)  
- [LinkedIn](https://www.linkedin.com/in/mohd-muzammil-109044290/)

---
