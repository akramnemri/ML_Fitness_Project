
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

calories_model = joblib.load('calories_model.pkl')
weight_model = joblib.load('weight_model.pkl')
rec_data = joblib.load('recommendation_model.pkl')

@app.route('/predict', methods=['POST'])
def predict_calories():
    data = request.json
    df = pd.DataFrame([data])
    return jsonify({'prediction': calories_model.predict(df)[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
