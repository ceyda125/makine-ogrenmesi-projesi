import streamlit as st
import pandas as pd
from joblib import load


model = load('eniyi.joblib')


st.title("Günlük Kalori İhtiyacı Tahmini")


boy = st.number_input("Boyunuz (cm):", min_value=0, max_value=250, step=1)
kilo = st.number_input("Kilonuz (kg):", min_value=0, max_value=200, step=1)
yas = st.number_input("Yaşınız:", min_value=0, max_value=120, step=1)
cinsiyet = st.selectbox("Cinsiyetiniz:", options=["Kadın", "Erkek"])
aktivite_seviyesi = st.selectbox(
    "Aktivite Seviyeniz:",
    options=["Hareketsiz", "Hafif", "Orta", "Yüksek"]
)

cinsiyet_mapping = {"Kadın": 0, "Erkek": 1}
aktivite_mapping = {
    "Hareketsiz": 0,
    "Hafif": 1,
    "Orta": 2,
    "Yüksek": 3
}

cinsiyet_numeric = cinsiyet_mapping[cinsiyet]
aktivite_numeric = aktivite_mapping[aktivite_seviyesi]


if st.button("Tahmini Hesapla"):
    input_data = pd.DataFrame({
        'Boy (cm)': [boy],
        'Kilo (kg)': [kilo],
        'Yaş (yıl)': [yas],
        'Cinsiyet': [cinsiyet_numeric],
        'Aktivite Seviyesi': [aktivite_numeric]
    })

    tahmin = model.predict(input_data)
    st.success(f"Günlük Kalori İhtiyacınız: {tahmin[0]:.2f} kcal")
