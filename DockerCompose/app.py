## Flask Application for Learning Docker

import time
import redis
from flask import Flask
import os

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            #cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def home():
    count = get_hit_count()
    return "Hello Ananda, I have been seen {} times.\n".format(count)
