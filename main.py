from flask import Flask, render_template, request, send_from_directory
from os import listdir
from os.path import isfile, join

app = Flask('app')

@app.route('/')
def index():
    return "<h1>0x0000 file hosting</h1>"
    # return '<br>'.join([f for f in listdir('files') if isfile(join('files', f))])

@app.route('/<file>')
def returnfile(file):
    try:
        return send_from_directory('files', file)
    except:
        return f"File '{file}'not found"

app.run(host='0.0.0.0', port=8080)