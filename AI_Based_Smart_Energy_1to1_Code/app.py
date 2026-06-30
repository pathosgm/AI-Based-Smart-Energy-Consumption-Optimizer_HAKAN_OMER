import streamlit as st
import pandas as pd
from energy_engine import predict_energy, optimize_energy, calculate_co2, forecast_energy

st.set_page_config(page_title="Smart Energy Optimizer", layout="centered")
st.title("AI-Based Smart Energy Consumption Optimizer")
st.write("This demo predicts energy usage and gives simple optimization advice.")

temperature = st.slider("Temperature (C)", 0, 45, 28)
humidity = st.slider("Humidity (%)", 0, 100, 55)
occupancy = st.slider("Occupancy", 0, 50, 12)
hour = st.slider("Hour of day", 0, 23, 18)

if st.button("Optimize Energy"):
    energy = predict_energy(temperature, humidity, occupancy, hour)
    decision, advice = optimize_energy(energy, occupancy, hour)
    co2 = calculate_co2(energy)
    forecast = forecast_energy(energy)

    st.subheader("Result")
    st.write("Predicted energy usage:", energy, "kWh")
    st.write("Decision:", decision)
    st.write("Advice:", advice)
    st.write("Estimated CO2 emission:", co2, "kg")

    data = pd.DataFrame({
        "Next hour": ["+1", "+2", "+3", "+4", "+5", "+6"],
        "Forecast kWh": forecast
    })

    st.subheader("Future Energy Forecast")
    st.bar_chart(data.set_index("Next hour"))
