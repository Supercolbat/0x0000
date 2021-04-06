from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os, json, string

from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET")
app.config['UPLOAD_FOLDER'] = "files"
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024


def urlexists(url):
    with open("urls.json") as f:
        urls = json.load(f)
        
        if url in urls.values():
            return True
        return False


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/wip')
def wip():
    return render_template("testing.html")


@app.route('/f/<file>')
def returnfile(file):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], file)
    except:
        return render_template("error.html", message="File '{}' not found'".format(file))

@app.route('/raw/<file>')
def returnraw(file):
    try:
        with open("files/"+file) as f:
            return "<pre>"+f.read()+"</pre>"
    except:
        return render_template("error.html", message="File '{}' not found'".format(file))



@app.route('/u/<url>')
def returnurl(url):
    with open("urls.json") as f:
        urls = json.load(f)

    if url in urls:
        return redirect(urls[url])
    else:
        return render_template("error.html", message="URL not found")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)

            file = request.files['file']

            if file.filename == '':
                flash("No selected file")
                return redirect(request.url)

            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # return redirect(url_for('upload', filename=filename))
        except RequestEntityTooLarge:
            flash("File too large")
        
    return render_template("upload.html")


@app.route('/shorten', methods=['GET', 'POST'])
def shorten():
    if request.method == 'POST':
        url = request.form["url"]

        if not urlexists(url):        
            with open("urls.json") as f:
                urls = json.load(f)
            
            urls[url] == ''.join(random.choices(string.letters + string.digits, k=8))
    
            with open("urls.json", "w") as f:
                json.dump(f, urls)
    
    return render_template("shorten.html")


app.run(host='0.0.0.0', port=8080)