from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@rabbitmq//')


@app.task
def add(x, y):
    return x + y


import requests


@app.task
def http_get(url):
    response = requests.get(url)
    # ... parsing the body ...

    return (response.status_code, result)


import nltk


@app.task
def get_pos(text, lang):
    tokens = nltkword_tokenize(text, lang)
    return (nltk.pos_tag(tokens=tokens))
