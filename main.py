from flask import Flask, render_template, url_for, redirect, request, send_from_directory

app = Flask('app')

@app.route('/')
def index():
    with open("files.txt") as f:
        return '<br>'.join(f.readlines())

@app.route('/cat.png')
def cat():
    print("RICK ROLLED")
    return redirect(url_for('files', filename='cat.mp4'))
    #return send_from_directory('files', 'cat.mp4')

@app.route('/dog.png')
def dog():
    return send_from_directory('files', 'dog.png')

@app.route('/mspaint.mp4')
def mspaint():
    return send_from_directory('files', 'mspaint.mp4')

@app.route('/roux.html')
def freerobux():
    return render_template('roux.html')

app.run(host='0.0.0.0', port=8080)