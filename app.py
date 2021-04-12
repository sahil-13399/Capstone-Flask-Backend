#!/bin/python3
import os
from flask import Flask, flash, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
from model import dyslexia,dyscalculia
from cloud_vision import handwrittenParser
from validate import validate_answers

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


@app.route('/api/dyscalculia/upload', methods=['POST'])
def upload_file():
    gender = 0 if str(request.form.get('gender')) == "Female" else 1
    age = int(request.form.get('age'))
    comp1 = int(request.form.get('comp1'))
    comp2 = str(request.form.get('comp2'))
    comp3 = str(request.form.get('comp3'))
    comp4 = int(request.form.get('comp4'))
    count1 = int(request.form.get('count1'))
    count2 = int(request.form.get('count2'))
    count3 = int(request.form.get('count3'))
    count4 = int(request.form.get('count4'))        
    compute1 = int(request.form.get('compute1'))
    compute2 = int(request.form.get('compute2'))
    compute3 = int(request.form.get('compute3'))
    compute4 = int(request.form.get('compute4'))
    time1 = str(request.form.get('time1'))
    time2 = str(request.form.get('time2'))
    time3 = str(request.form.get('time3'))
    time4 = str(request.form.get('time4'))
    geo1 = str(request.form.get('geo1'))
    geo2 = str(request.form.get('geo2'))
    geo3 = int(request.form.get('geo3'))
    geo4 = str(request.form.get('geo4'))
    l1 = [comp1,comp2,comp3,comp4]
    l2 = [count1,count2,count3,count4]
    l3 = [compute1,compute2,compute3,compute4]
    l4 = [time1,time2,time3,time4]
    l5 = [geo1,geo2,geo3,geo4]
    #score1,score2,score3,score4,score5 = validate_answers(l1,l2,l3,l4,l5)
    #result = dyscalculia([[gender,age,score1,score2,score3,score4,score5]])
    #return jsonify({'Status':int(result[0])})
    return jsonify({'Status':geo1})

@app.route('/api/dyslexia/upload',methods=['POST'])
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
