#!/usr/bin/env python
# coding: utf-8

import requests

url = "http://localhost:9696/predict"

client_id = "xyz-123"
client = {"job": "retired", "duration": 445, "poutcome": "success"}

if __name__ == "__main__":
    response = requests.post(url, json=client).json()
    proba = round(response["approval_probability"], 3)

    if response["approve"] == True:
        status = "approved"
    else:
        status = "rejected"
    print(
        f"Credit request for client {client_id} is {status} with probability of {proba}"
    )
