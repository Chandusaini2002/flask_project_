from flask import Flask ,request, render_template
import os
from werkzeug.utils import secure_filename
import time
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the form has the file part
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']

    # If no file is selected
    if file.filename == '':
        return "No selected file", 400

    if file:
        # Secure the filename and add a timestamp
        filename = f"{int(time.time())}_{secure_filename(file.filename)}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the file
        file.save(filepath)
        return f"File uploaded successfully! Saved as: {filepath}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

