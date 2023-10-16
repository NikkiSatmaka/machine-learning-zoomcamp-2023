#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import joblib
from flask import Flask, jsonify, request

vectorizer_file = "dv.bin"
model_file = "model2.bin"

with open(vectorizer_file, "rb") as f:
    dv = joblib.load(f)

with open(model_file, "rb") as f:
    model = joblib.load(f)

app = Flask("credit_approval")


@app.route("/predict", methods=["POST"])
def predict():
    client = request.get_json()

    X = dv.transform(client)
    y_pred = model.predict_proba(X)[0, 1]
    approved = y_pred >= 0.5

    result = {
        "approval_probability": float(y_pred),
        "approve": bool(approved),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
