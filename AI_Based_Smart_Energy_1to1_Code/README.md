# AI-Based Smart Energy Consumption Optimizer

This is a simple Python and Streamlit demo project for smart building energy optimization.

## Files

- `app.py` - Streamlit web interface
- `energy_engine.py` - prediction, optimization, CO2, and forecast logic
- `main.py` - command-line version
- `requirements.txt` - required packages

## Run the web application

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

## Demo values

- Temperature: 28
- Humidity: 55
- Occupancy: 12
- Hour of day: 18

The system predicts energy usage, gives a decision, estimates CO2 emission, and displays a six-hour forecast chart.
