import streamlit as st
import pandas as pd
import joblib

model = joblib.load("aqi_model.pkl")

st.title("🌍 Air Quality Index Prediction")

st.markdown(
    "[📂 View Full Project Source Code on GitHub](https://github.com/Likhin1404/AQI-Prediction-Using-Machine-Learning)"
)
st.write("Enter pollutant AQI values")

co = st.number_input("CO AQI Value")
ozone = st.number_input("Ozone AQI Value")
no2 = st.number_input("NO2 AQI Value")
pm25 = st.number_input("PM2.5 AQI Value")
lat = st.number_input("Latitude")
lng = st.number_input("Longitude")


def classify_aqi(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"

    elif aqi <= 200:
        return "Unhealthy"

    elif aqi <= 300:
        return "Very Unhealthy"

    else:
        return "Hazardous"


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

    st.success(f"Predicted AQI: {prediction:.2f}")
    st.success(f"AQI Category: {category}")
