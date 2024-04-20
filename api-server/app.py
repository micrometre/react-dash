import os
from flask import Flask, Response, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
import logging
from datetime import date 
import subprocess
import os
import re

UPLOAD_FOLDER = '../public/uploads'
ALLOWED_EXTENSIONS = {'mp4', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
logging.getLogger('flask_cors').level = logging.DEBUG

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            alpr_file = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            alpr_arg1 = "-i"
            alpr_arg2 = "-c"
            alpr_arg3 = "copy"
            alpr_arg4 = "out.mkv"
            output = subprocess.check_output(['ffmpeg',str(alpr_arg1), str(alpr_file), str(alpr_arg2), str(alpr_arg3), str(alpr_arg4) ]).decode('utf-8')
            print(output)
            return redirect(url_for('upload_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return {
        "token": 'test123'
    }


@app.route("/video")
def video():
    data = "../public/uploads/alprVideo.mp4"
    print(type(data))
    return send_file(data)