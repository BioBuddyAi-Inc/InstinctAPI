from flask import Flask, request, jsonify
import base64
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
from flask_cors import CORS


app = Flask(__name__)

@app.route('/')
def home():
    return "🐍 Snake Classifier API is running. Use POST /classify."

@app.route("/classify", methods=["POST"])
def classify_image():
    print("🔥 Received request to /classify")

    try:
        data = request.get_json(force=True)  # force=True just in case header is off
        print("📦 Parsed JSON data:", data)

        image_b64 = data.get("image_base64")
        if not image_b64:
            print("🚫 No image_base64 in request!")
            return jsonify({"error": "No image provided"}), 400

        print("🧬 Decoding base64 image...")
        image_data = base64.b64decode(image_b64)
        np_arr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        print("🧪 Running fake classification")
        label = "Snake"
        score = 0.95

        print("✅ Returning result:", {"label": label, "score": score})
        return jsonify({"label": label, "score": score})
    
    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
