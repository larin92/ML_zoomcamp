## 5. Deployment

* [Study materials](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment)

* [Lesson's code](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment/code)

* [Homework task](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/cohorts/2023/05-deployment/homework.md)

* [Extra notes](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/05a_deployment.md)

* [docker (community notes)](https://github.com/ayoub-berdeddouch/mlbookcamp-homeworks/blob/main/Deployment/README.md)

* [docker cheatsheet](https://gist.github.com/ziritrion/1842c8a4c4851602a8733bba19ab6050#docker)

---
* [Dataset](https://www.kaggle.com/datasets/kapturovalexander/bank-credit-scoring/data) (not used explicitly)

---
## [Homework task](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/cohorts/2023/05-deployment/homework.md)

Basically homework is about predicting whether client with specified info will get a credit. Response looks like this (`[[negative positive]]` outcome): 

```
[[0.09806907 0.90193093]]
```
Here "client gets credit" with `0.9` certainty. Can be thresholded for `true/false` or human-language outcomes, but that's not in the task of the homework.

## Docker serving

(for [local non-docker serving](#local-serving))

([Testing/using](#testingusing))

To run docker container:
- build image from `Dockerfile` (`.` is important):
``` 
docker build -f Dockerfile -t homework5:01 .
```
- run the container:
```
docker run -d --name homework5 -p 9696:9696 homework5:01
```
- stop container / cleanup:
```
docker rm $(docker stop homework5)
```

> Notes: 
>>specifying --name lets us easily stop/cleanup by name.
>
>> run flags: 
>> - -d is short for --detach, which means you just run the container and then detach from it. Essentially, you run container in the background.
>> - -it is short for --interactive + --tty. When you docker run with this command it takes you straight inside the container.

## Local serving

- Requirements

The only thing you need to install is:
`scikit-learn==1.3.1`
and the preferred serving library ([flask](https://flask.palletsprojects.com/en/3.0.x/) alone is enough, optionally - a WSGI like [gunicorn](https://docs.gunicorn.org/en/stable/run.html)/[waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/index.html)/[gevent.pywsgi](http://www.gevent.org/api/gevent.pywsgi.html)):
```
pip install flask scikit-learn==1.3.1 gunicorn waitress gevent
```

- gunicorn serve (Unix):
```
gunicorn --bind localhost:9696 script:app
```

- waitress serve (Windows):
```
waitress-serve --listen=localhost:9696 script:app
```

Can also be served just via [flask](https://flask.palletsprojects.com/en/3.0.x/) or [gevent.pywsgi](http://www.gevent.org/api/gevent.pywsgi.html), although according parts in [script.py](script.py) should be uncommented. Running both options via terminal looks like this:
```
python script.py
```

## Testing/using
For testing [test.py](test.py) can be used (uses `requests` library), or just `curl` (`/predict1` and `/predict2` are endpoints for 2 different models):

```
curl 127.0.0.1:9696/ping
```

```
curl -i -X POST -H "Content-Type: application/json" -d "{\"job\": \"unknown\", \"duration\": 270, \"poutcome\": \"failure\"}" http://localhost:9696/predict1
```

```
curl -i -X POST -H "Content-Type: application/json" -d "{\"job\": \"retired\", \"duration\": 445, \"poutcome\": \"success\"}" http://localhost:9696/predict2
```
