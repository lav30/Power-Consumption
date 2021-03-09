
import flask
from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import numpy as np
from openpyxl import load_workbook


app = Flask(__name__)

df = pd.read_excel('Folds5x2_pp.xlsx')
model = load_model('Final XGBoost Model 3March2021')
cols = ['AT', 'V', 'AP', 'RH']
data = df.sample(frac=0.8, random_state=786)
data_unseen = df.drop(data.index)
data.reset_index(drop=True, inplace=True)
data_unseen.reset_index(drop=True, inplace=True)


@app.route('/')
def home():
    return render_template("app.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen)
    prediction = int(prediction.Label[0])
    return render_template('app.html',pred='Expected Power Output in MW : {}'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.Label[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
