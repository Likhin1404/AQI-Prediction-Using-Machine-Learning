import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("aqi_model.pkl")

# Page Title
st.title("🌍 Air Quality Index Prediction")

# GitHub Repository Link
st.markdown(
    "[📂 View Full Project Source Code on GitHub](https://github.com/Likhin1404/AQI-Prediction-Using-Machine-Learning)"
)

# Project Description
st.info(
    """
    This is an academic Machine Learning project developed to predict
    Air Quality Index (AQI) using pollutant data.

    Sample values are already provided below for testing.
    """
)

# Input Section
st.subheader("Enter Pollutant AQI Values")

co = st.number_input("CO AQI Value", value=1.0)
ozone = st.number_input("Ozone AQI Value", value=36.0)
no2 = st.number_input("NO2 AQI Value", value=0.0)
pm25 = st.number_input("PM2.5 AQI Value", value=51.0)
lat = st.number_input("Latitude", value=44.7444)
lng = st.number_input("Longitude", value=44.2031)


# AQI Classification Function
def classify_aqi(aqi):

    if aqi <= 50:
        return "🟢 Good"

    elif aqi <= 100:
        return "🟡 Moderate"

    elif aqi <= 150:
        return "🟠 Unhealthy for Sensitive Groups"

    elif aqi <= 200:
        return "🔴 Unhealthy"

    elif aqi <= 300:
        return "🟣 Very Unhealthy"

    else:
        return "⚫ Hazardous"


# Prediction Button
if st.button("Predict AQI"):

    sample = pd.DataFrame(
        [[co, ozone, no2, pm25, lat, lng]],
        columns=[
            "CO AQI Value",
            "Ozone AQI Value",
            "NO2 AQI Value",
            "PM2.5 AQI Value",
            "lat",
            "lng"
        ]
    )

    prediction = model.predict(sample)[0]

    category = classify_aqi(prediction)

    st.success(f"Predicted AQI Value: {prediction:.2f}")
    st.success(f"AQI Category: {category}")

# Footer
st.markdown("---")
st.caption(
    "Academic Machine Learning Project | Python • Scikit-Learn • Streamlit"
)
