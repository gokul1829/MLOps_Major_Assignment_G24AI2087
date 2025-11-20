# app.py
import os
import joblib
import numpy as np
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from sklearn.preprocessing import StandardScaler
from PIL import Image

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
saved = joblib.load("savedmodel.pth")
model = saved["model"]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Helper: convert uploaded face image to 1D vector expected by Olivetti (64x64 greyscale)
def preprocess_image(filepath):
    img = Image.open(filepath).convert('L').resize((64,64))
    arr = np.asarray(img, dtype=float)
    arr = arr.flatten()
    # Olivetti pixel values are float between 0 and 1; scale appropriately
    arr = arr / 255.0
    return arr.reshape(1, -1)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            x = preprocess_image(path)
            pred = model.predict(x)[0]
            return render_template("result.html", pred=pred, filename=filename)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
