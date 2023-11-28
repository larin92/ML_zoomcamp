import numpy as np
import tflite_runtime.interpreter as tflite
# import tensorflow.lite as tflite
from io import BytesIO
from urllib import request
from PIL import Image
import os

# Get model path from the environment variable
model_path = os.getenv('MODEL_PATH', 'bees-wasps.tflite')

class_indicies = {'bee': 0, 'wasp': 1}

interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def download_image(url) -> Image:
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def preprocess_image(img: Image, target_size) -> np.ndarray:
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    x = np.asarray(img)/255
    return x.astype(np.float32)

def predict(url):
    img = download_image(url)
    x = preprocess_image(img, (150, 150))
    interpreter.set_tensor(input_index, [x])
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_index)
    return {'result': str(output_data[0][0]), **class_indicies}

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
