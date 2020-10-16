from flask import Flask, render_template, send_from_directory, request
from werkzeug.utils import secure_filename
from database import *
import os, json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET")
app.config['UPLOAD_FOLDER'] = "/files"
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

BLACKLISTED_EXTENSIONS = [
    "htm",
    "html"
]


def validate(filename):
    return '.' in filename and \
           not filename.rsplit('.', 1)[1].lower() in BLACKLISTED_EXTENSIONS


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/test')
def test():
    return render_template("testing.html")

@app.route('/<file>')
def returnfile(file):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], file)
    except:
        return f"File '{file}' not found"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and validate(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
        
    return render_template("upload.html")

app.run(host='0.0.0.0', port=8080)