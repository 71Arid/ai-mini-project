import requests
import json

# Sample patient data (28 features)
features = [
    35, 3.0, 17.0, 2.0, 1.0, 5.0, 0.5,    # Demographics/Smoking (7)
    1.0, 3.0, 0.0, 0.0,                    # Contraceptives (4)
    1.0, 2.0, 0.0, 0.0, 1.0, 0.0, 1.0,     # STDs (7)
    2,                                      # STDs: Number of diagnosis (1)
    0, 0, 0, 0, 0, 0, 0               # Diagnostic flags (8)
]

response = requests.post(
    "http://127.0.0.1:5000/predict",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"features": features})
)

print("Prediction:", response.json())