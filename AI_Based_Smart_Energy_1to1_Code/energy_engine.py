def predict_energy(temperature, humidity, occupancy, hour):
    energy = 8
    energy = energy + temperature * 0.25
    energy = energy + humidity * 0.05
    energy = energy + occupancy * 0.8

    if 17 <= hour <= 21:
        energy = energy + 5

    return round(energy, 2)


def optimize_energy(predicted_energy, occupancy, hour):
    if occupancy == 0:
        return "LOW POWER MODE", "Turn off lights and reduce HVAC because the building is empty."

    if predicted_energy >= 30:
        return "OPTIMIZE", "Energy use is high. Reduce HVAC load and avoid unnecessary devices."

    if 17 <= hour <= 21:
        return "PEAK HOUR WARNING", "Peak hour detected. Shift heavy loads to a later time."

    return "NORMAL", "Energy consumption is in a normal range."


def calculate_co2(energy):
    return round(energy * 0.4, 2)


def forecast_energy(predicted_energy):
    values = []
    for i in range(1, 7):
        values.append(round(predicted_energy + i * 0.8, 2))
    return values
