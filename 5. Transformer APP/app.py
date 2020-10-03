import pickle
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline('sentiment-analysis')

@app.route('/predict', methods=['POST'])
def predict():
    text = str(request.get_json(force=True)['text'])
    result = classifier(text)[0]
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
