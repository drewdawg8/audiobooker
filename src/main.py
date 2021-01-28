from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from werkzeug.utils import secure_filename
import os
from functions import *



app = Flask(__name__)

UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/success/<name>",methods = ['POST', 'GET'])
def success(name):
    text = parse_text(name)
    os.remove(name)
    return render_template("success.html", value = text)

@app.route('/read')
def read():
    read_text()
    return '', 204 # no content


@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for("success", name = filename))
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
