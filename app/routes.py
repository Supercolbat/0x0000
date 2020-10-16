from flask import Flask, render_template, send_from_directory
from app import app

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/<file>')
def returnfile(file):
    try:
        return send_from_directory('files', file)
    except:
        return f"File '{file}'not found"

app.run(host='0.0.0.0', port=8080)