import streamlit as st
import pandas as pd
import joblib
import os

# Configuration de la page
st.set_page_config(
    page_title="Prédiction de l'Anémie",
    page_icon="🏥",
    layout="centered"
)

# Chargement du modèle
@st.cache_resource
def load_model():
    model_path = os.path.join('models', 'best_model.pkl')
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        return None

model = load_model()

# Interface utilisateur
st.title("🏥 Assistant de Diagnostic de l'Anémie")
st.write("""
Cette application utilise le Machine Learning pour aider à détecter l'anémie 
en se basant sur vos résultats d'analyse de sang.
""")

st.info("ℹ️ Veuillez entrer les valeurs de votre test sanguin ci-dessous.")

# Formulaire de saisie
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Genre", options=[("Homme", 1), ("Femme", 0)], format_func=lambda x: x[0])
        hemoglobin = st.number_input("Hémoglobine (g/dL)", min_value=0.0, max_value=25.0, value=12.0, step=0.1)
        mch = st.number_input("MCH (pg)", min_value=0.0, max_value=50.0, value=25.0, step=0.1)
        
    with col2:
        mchc = st.number_input("MCHC (g/dL)", min_value=0.0, max_value=50.0, value=30.0, step=0.1)
        mcv = st.number_input("MCV (fL)", min_value=0.0, max_value=150.0, value=85.0, step=0.1)
        
    submit_button = st.form_submit_button("Analyser les résultats")

# Traitement de la prédiction
if submit_button:
    if model is not None:
        # Préparation des données
        input_data = pd.DataFrame({
            'Gender': [gender[1]],
            'Hemoglobin': [hemoglobin],
            'MCH': [mch],
            'MCHC': [mchc],
            'MCV': [mcv]
        })
        
        # Prédiction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        st.divider()
        
        if prediction == 1:
            st.error(f"⚠️ **Résultat : Probabilité d'Anémie Détectée**")
            st.write(f"Confiance du modèle : {probability:.2%}")
            st.warning("Conseil : Veuillez consulter un médecin pour une analyse approfondie.")
        else:
            st.success(f"✅ **Résultat : Pas d'Anémie Détectée**")
            st.write(f"Confiance du modèle : {(1-probability):.2%}")
            st.write("Vos résultats semblent être dans les normes.")
    else:
        st.error("Le modèle n'a pas pu être chargé. Assurez-vous que 'models/best_model.pkl' existe.")

# Footer
st.divider()
st.caption("Développé dans le cadre du projet Machine Learning - 2026")
