FROM agrigorev/zoomcamp-bees-wasps:v2
# FROM public.ecr.aws/lambda/python:3.10
# COPY bees-wasps-v2.tflite .

COPY lambda_function.py .
COPY requirements.txt .

RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
RUN pip install --no-cache-dir -r requirements.txt


ENV MODEL_PATH=bees-wasps-v2.tflite

CMD [ "lambda_function.lambda_handler" ]
