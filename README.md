# ML Flask API Deployment

Deploy your machine learning model as a Flask API.

## 🚀 Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/ml_flask_api.git
   cd ml_flask_api
    ```
2. **Run setup script**:
    linux/mac:
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```
    Windows (PowerShell):
    ```powershell
    .\setup.ps1
    ```
3. **Running the API**:
    ```bash
    python app.py # dev
    gunicorn -w 4 app:app # production
    ```
    The app will run at http://127.0.0.1:5000
4. **Access the API**:
    Send a POST request to /predict with input features:
    ```bash
    curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d '{
        "features": [
        35, 3.0, 17.0, 2.0, 1.0, 5.0, 0.5, 1.0, 3.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0, 1.0, 0.0, 1.0, 2, 0, 0, 0, 0, 0, 0, 0, 0
        ]
    }'
    ```
    or run to test api
    ```bash
    python test-request.py
    ```