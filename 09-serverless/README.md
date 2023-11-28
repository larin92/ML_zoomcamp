## 9. Serverless Deep Learning

[Study materials]
https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/09-serverless

[Lesson's code]
https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/09-serverless/code

[Homework task]
https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/cohorts/2023/09-serverless/homework.md

----
This homework is about classifying picture as `bee` or `wasp`.

Result/response looks like this: 
```
{'result': '0.6592137', 'bee': 0, 'wasp': 1}
```
Here, model classified [picture](https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg) as `wasp` (result over 0.5 = `wasp`).

## Script-style use

- Requirements
```bash
pip install -r requirements.txt
```

- Usage/testing (can be used with any `url`)
```bash
python test.py
```

## Serving/deploy

Solution is built for deploy to `AWS Lambda`, but we can run/test it locally.

To run docker container locally:
- build image from `Dockerfile`:
```bash
docker build -f Dockerfile -t bee-or-wasp .
```
- run the container:
```bash
docker run -it --rm -p 9000:8080 bee-or-wasp
```

To test locally using `curl`:

- Windows:
```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"url\": \"https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg\"}"
```
- Unix:
```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"url": "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"}'
```

> localhost link looks like this for local usage/testing with the help of [AWS RIE](https://github.com/aws/aws-lambda-runtime-interface-emulator/#test-an-image-with-rie-included-in-the-image)
