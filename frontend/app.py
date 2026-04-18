import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://backend:8000/predict"

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title(" House Price Prediction")
st.write("Enter the features below to predict house price")

# Input fields
MedInc = st.number_input("Median Income", min_value=0.0)
HouseAge = st.number_input("House Age", min_value=0.0)
AveRooms = st.number_input("Average Rooms", min_value=0.0)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.0)
Population = st.number_input("Population", min_value=0.0)
AveOccup = st.number_input("Average Occupancy", min_value=0.0)
Latitude = st.number_input("Latitude", value=34.0)
Longitude = st.number_input("Longitude", value=-118.0)

# Predict button
if st.button("Predict"):
    payload = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude,
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"Predicted House Price: {prediction:.2f}")
        else:
            st.error("Prediction failed")

    except Exception as e:
        st.error(f"Error: {e}")