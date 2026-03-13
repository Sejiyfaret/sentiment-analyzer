import streamlit as st
from joblib import load
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import nltk

# Télécharger les ressources nécessaires
nltk.download('punkt')

# Charger le modèle
model = load('model.joblib')

# Fonction de nettoyage
def clean_text(text):
    soup = BeautifulSoup(text, "html.parser")
    cleaned_text = soup.get_text()
    cleaned_text = ''.join(e for e in cleaned_text if e.isalnum() or e.isspace())
    return cleaned_text.lower()

# Interface
st.title("🧠 VOTRE ANALYSEUR SENTIMENTAL")
st.write("Bienvenue dans mon application d'analyse de sentiment basée sur les tweets !")

text = st.text_area("✍️ Entrez votre texte ici :", "Type something...")

if st.button("Analyser"):
    cleaned = clean_text(text)
    prediction = model.predict([cleaned])[0]
    proba = model.predict_proba([cleaned])[0]

    sentiment = "Négatif" if prediction == 1 else "Positif/Neutre"
    st.write(f"### 💬 Sentiment détecté : **{sentiment}**")
    st.write(f"📊 Probabilité : Négatif = {proba[1]:.2f}, Positif/Neutre = {proba[0]:.2f}")
