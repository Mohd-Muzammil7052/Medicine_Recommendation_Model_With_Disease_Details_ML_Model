import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load data
dis_sym = pd.read_csv("symtoms_df.csv")
precautions = pd.read_csv("precautions_df.csv")
workout = pd.read_csv("workout_df.csv")
description = pd.read_csv("description.csv")
diets = pd.read_csv("diets.csv")
medications = pd.read_csv("medications.csv")

# Load model and encoder
with open('model_svc.pkl', 'rb') as f:
    model_svc = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
    enc = pickle.load(f)

# Function to fetch details about the disease
def about_disease(dis):
    desc = " ".join(description[description['Disease'] == dis]['Description'])
    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.flatten().tolist()
    med = " ".join(medications[medications['Disease'] == dis]['Medication'])
    diet = diets[diets['Disease'] == dis]['Diet'].values.tolist()
    wrk = workout[workout['disease'] == dis]['workout'].values.tolist()
    return desc, pre, med, diet, wrk

symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}
# Prediction function
def predict_disease(symptoms):
    input_vec = np.zeros(len(symptoms_dict))
    for symptom in symptoms:
        if symptom in symptoms_dict:
            input_vec[symptoms_dict[symptom]] = 1
    prediction = enc.inverse_transform(model_svc.predict(input_vec.reshape(1, -1)))[0]
    return prediction

# Streamlit app
st.title("DocBot AI 💻🤖")

st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-size: 20px !important;
    }
    h1 {
        font-size: 36px !important;
    }
    h2 {
        font-size: 28px !important;
    }
    h3 {
        font-size: 24px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Initialize session state for the prediction
if "predicted_disease" not in st.session_state:
    st.session_state.predicted_disease = None
    st.session_state.details = {}

# Input for symptoms
symptoms = st.text_input("Enter your Symptoms (comma-separated):")
user_symptom = [s.strip() for s in symptoms.split(',') if s.strip()]

# Predict button
if st.button("Predict"):
    if user_symptom:
        prediction = predict_disease(user_symptom)
        desc, pre, med, diet, wrk = about_disease(prediction)
        st.session_state.predicted_disease = prediction
        st.session_state.details = {
            "Description": desc,
            "Precautions": pre,
            "Medication": med,
            "Diet": diet,
            "Workouts": wrk,
        }
        st.success(f"Predicted Disease: {prediction}")
    else:
        st.warning("Please enter at least one symptom.")

# Display buttons only if a disease is predicted
if st.session_state.predicted_disease:
    st.subheader(f"Predicted Disease: {st.session_state.predicted_disease}")

    # Interactive buttons for disease details
    if st.button("Description"):
        st.write(f"**Description:** {st.session_state.details['Description']}")
        
    if st.button("Precautions"):
        st.write("**Precautions:**")
        for i, p in enumerate(st.session_state.details['Precautions'], start=1):
            st.write(f"{i}. {p}")

    if st.button("Medication"):
        st.write(f"**Medication:** {st.session_state.details['Medication']}")

    if st.button("Diet"):
        st.write("**Diet:**")
        for d in st.session_state.details['Diet']:
            st.write(f"- {d}")

    if st.button("Workouts"):
        st.write("**Workouts:**")
        for w in st.session_state.details['Workouts']:
            st.write(f"- {w}")
