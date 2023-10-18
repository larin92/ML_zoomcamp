import os
import pickle
from flask import Flask
from flask import request
from flask import jsonify

# q3
# client = {"job": "retired", "duration": 445, "poutcome": "success"}
# response (answer=last): [[0.09806907 0.90193093]]

# q4
# client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
# response (answer=last): [[0.86031053 0.13968947]]

# q6
# client = {"job": "retired", "duration": 445, "poutcome": "success"}
# response (answer=last): [[0.27306305364457695,0.726936946355423]]

# model1/dv1 just in case (will leave links in readme):
# PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2023/05-deployment/homework
# wget $PREFIX/model1.bin
# wget $PREFIX/dv.bin
# (renamed dv to dv1 locally)

app = Flask('predict')

model1 = None
dv1 = None
if os.path.exists('model1.bin') and os.path.exists('dv1.bin'):
    with open('model1.bin', 'rb') as model_bin, open('dv1.bin', 'rb') as dv_bin:
        model1 = pickle.load(model_bin)
        dv1 = pickle.load(dv_bin)

# beware, naming/paths
model2 = None
dv2 = None
if os.path.exists('model2.bin') and os.path.exists('dv.bin'):
    with open('model2.bin', 'rb') as model_bin, open('dv.bin', 'rb') as dv_bin:
        model2 = pickle.load(model_bin)
        dv2 = pickle.load(dv_bin)

@app.route('/predict1', methods=['POST'])
def predict1():
    if not (model1 and dv1):
        return ("model1 or dv1 not found")
    client = request.get_json()
    result = model1.predict_proba(dv1.transform(client))
    # print(result)

    return jsonify(result.tolist())

@app.route('/predict2', methods=['POST'])
def predict2():
    if not (model2 and dv2):
        return ("model2 or dv2 not found, use /predict1 endpoint")
    client = request.get_json()
    result = model2.predict_proba(dv2.transform(client))
    # print(result)

    return jsonify(result.tolist())

@app.route('/ping', methods=['GET'])
def ping():
    return "PONG"

# flask serving without WSGI, run via `python scipt.py`
# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=9696)

# alternative WSGI, tried out
# from gevent.pywsgi import WSGIServer
# http_server = WSGIServer(('localhost', 9696), app)
# http_server.serve_forever()
