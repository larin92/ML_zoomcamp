import requests

# ping endpoint
print(requests.get('http://127.0.0.1:9696/ping'))

# /predict1 and /predict2 endpoints use different models
url1 = 'http://127.0.0.1:9696/predict1'
url2 = 'http://127.0.0.1:9696/predict2'
client1 = {"job": "unknown", "duration": 270, "poutcome": "failure"}
client2 = {"job": "retired", "duration": 445, "poutcome": "success"}
print(requests.post(url1, json=client1).json())
print(requests.post(url2, json=client2).json())

