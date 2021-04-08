#!/bin/python3
import os
from flask import Flask, flash, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
from model import dyslexia,dyscalculia
from cloud_vision import handwrittenParser

from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello, World!'


UPLOAD_FOLDER = './static/test'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/dyslexia/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            response = jsonify({'result': "file Upload failed!!!"})
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        file = request.files['file']
        gender = 0 if str(request.form.get('gender')) == "Female" else 1
        n_language = 0 if str(request.form.get('nlanguage')) == "No" else 1
        o_language = 0 if str(request.form.get('olanguage')) == "No" else 1
        age = int(request.form.get('age'))
        
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            response = jsonify({'result': "file Upload failed!!!"})
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            hits,misses,accuracy = handwrittenParser(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        result = dyslexia([gender,n_language,o_language,age,hits,misses,accuracy])
        response = jsonify({'result': result})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
            

    

@app.route('/api',methods=['POST'])
def test_func():
    gender = 0 if str(request.form.get('gender')) == "Female" else 1
    n_language = 0 if str(request.form.get('nlanguage')) == "No" else 1
    o_language = 0 if str(request.form.get('olanguage')) == "No" else 1
    age = int(request.form.get('age'))
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    hits,misses,accuracy = handwrittenParser(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    result = dyslexia([[gender,n_language,o_language,age,hits,misses,accuracy]])
    print(str(hits)+" "+str(misses)+" "+str(accuracy))
    return jsonify({'Status':int(result[0])})

if __name__ == '__main__':
    app.run(debug=True)
