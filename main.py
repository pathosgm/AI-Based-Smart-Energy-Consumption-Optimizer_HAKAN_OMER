from energy_engine import predict_energy, optimize_energy, calculate_co2, forecast_energy

print("AI-Based Smart Energy Consumption Optimizer")
print("--------------------------------------------")

temperature = int(input("Enter temperature (C): "))
humidity = int(input("Enter humidity (%): "))
occupancy = int(input("Enter occupancy: "))
hour = int(input("Enter hour of day (0-23): "))

energy = predict_energy(temperature, humidity, occupancy, hour)
decision, advice = optimize_energy(energy, occupancy, hour)
co2 = calculate_co2(energy)
forecast = forecast_energy(energy)

print("\nResult")
print("------")
print("Predicted energy usage:", energy, "kWh")
print("Decision:", decision)
print("Advice:", advice)
print("Estimated CO2 emission:", co2, "kg")
print("Six-hour forecast:", forecast)
