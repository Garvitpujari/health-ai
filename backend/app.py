from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_risk

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "HealthAI Backend Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    result = predict_risk(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
