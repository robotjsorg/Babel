import requests
import redis
import json
from fastapi import FastAPI

rd = redis.Redis(host="localhost", port=6379, db=0)

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello, World!"

@app.get("/messages/{uuids}")
def read_messages(uuids: str):
    cache = rd.get(uuids)
    if cache:
        print("cache hit")
        return json.loads(cache)
    else:
        print("cache miss")
        r = requests.get("http://localhost:8000/messages/{uuids}")
        rd.set(uuids, r.text)
        return r.json()

