from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler (if any)
MODEL_PATH = "model/Cancer-model.joblib"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Error loading model/scaler: {str(e)}")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data
        data = request.json
        
        # Validate input
        if not data or "features" not in data:
            return jsonify({"error": "Missing 'features' in request"}), 400
        
        features = np.array(data["features"]).reshape(1, -1)
        
        # Predict
        prediction = model.predict(features)
        
        # Return response
        return jsonify({
            "prediction": prediction.tolist()[0],  # Assuming single output
            "status": "success"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)