from flask import Flask, request, jsonify
from .models import rule_based_prediction

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['POST'])
def predict():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    result = rule_based_prediction(num1, num2)
    return jsonify(result)
