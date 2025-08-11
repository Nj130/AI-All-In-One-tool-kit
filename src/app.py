from flask import Flask, request, jsonify
import pickle
from extractor import extract_features
from enricher import enrich_features
import pandas as pd

app = Flask(__name__)

with open('src/model/vulnerability_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    temp_path = 'temp_scan.json'
    with open(temp_path, 'w') as f:
        import json
        json.dump(data, f)
    df = extract_features(temp_path)
    df = enrich_features(df)
    preds = model.predict(df)
    df['prediction'] = preds
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)