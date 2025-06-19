from flask import Flask, request, jsonify, render_template
from model_utils import train_model, predict_image
import os

app = Flask(__name__, static_folder='static', template_folder='static')
LABELS = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    global LABELS
    data_dir = request.form.get("data_dir", "pistachio_dataset")
    LABELS = train_model(data_dir)
    return jsonify({"message": "Model trained", "labels": LABELS})

@app.route('/predict', methods=['POST'])
def predict():
    global LABELS
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image = request.files['image']
    image_path = os.path.join("static", "upload.jpg")
    image.save(image_path)
    label = predict_image(image_path, LABELS)
    return jsonify({"prediction": label})

@app.route('/labels', methods=['GET'])
def get_labels():
    global LABELS
    if not LABELS:
        return jsonify({"labels": [], "message": "Model not yet trained."}), 200
    return jsonify({"labels": LABELS})

if __name__ == "__main__":
    app.run(debug=True)