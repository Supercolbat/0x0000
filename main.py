from flask import Flask, render_template, request, send_from_directory
from os import listdir
from os.path import isfile, join

app = Flask('app')

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