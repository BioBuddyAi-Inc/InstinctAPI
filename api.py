from flask import Flask, request, jsonify
import base64
import numpy as np
import cv2
from flask_cors import CORS
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)
CORS(app)

# Load your model once at startup
model = load_model("snake_model.h5")

API_KEYS = {"biobuddy", "testkey123"}

@app.before_request
def check_api_key():
    if request.endpoint == 'home':
        return
    key = request.headers.get("X-API-Key")
    if key not in API_KEYS:
        return jsonify({"error": "Invalid or missing API key"}), 403

@app.route('/')
def home():
    return jsonify({
        "status": "OK",
        "message": "Welcome to InstinctAPI — POST your image_base64 to /classify"
    })

@app.route("/classify", methods=["POST"])
def classify_image():
    print("🔥 Received request to /classify")

    try:
        data = request.get_json(force=True)
        image_b64 = data.get("image_base64")
        if not image_b64:
            return jsonify({"error": "No image provided"}), 400

        print("📦 Decoding image")
        image_data = base64.b64decode(image_b64)
        np_arr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        print("🧪 Preprocessing image")
        img = cv2.resize(img, (224, 224))  # adjust if your model uses a different size
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        print("🧬 Running model prediction")
        prediction = model.predict(img)[0]

        label = "Snake" if prediction[0] > 0.5 else "Not Snake"
        score = float(prediction[0]) if prediction[0] > 0.5 else float(1 - prediction[0])

        print("✅ Prediction complete:", {"label": label, "score": score})
        return jsonify({"label": label, "score": round(score, 3)})
    
    except Exception as e:
        print("❌ Error during classification:", str(e))
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
