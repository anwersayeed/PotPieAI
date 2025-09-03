import json
import random
import redis
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.config import settings

router = APIRouter()

# Redis client
rd = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    password=settings.redis_password,
    decode_responses=True
)

@router.get("/name/{user_name}")
def greeting(user_name: str):
    cache = rd.get(user_name)
    if cache:
        print("cache hit!")
        return json.loads(cache)
    else:
        print("cache miss!")
        r = {"user": user_name.title(), "passkey": random.randint(0, 99999)}
        rd.set(user_name, json.dumps(r))
        return JSONResponse(r)

@router.post("/set")
def set_key(key: str = Body(...), value: str = Body(...)):
    rd.set(key, value)
    return {"status": "success", "key": key, "value": value}

@router.get("/get/{key}")
def get_key(key: str):
    value = rd.get(key)
    if value:
        return {"key": key, "value": value}
    return {"error": "Key not found"}

@router.delete("/delete/{key}")
def delete_key(key: str):
    result = rd.delete(key)
    if result == 1:
        return {"status": "deleted", "key": key}
    return {"error": "Key not found"}

@router.get("/keys")
def list_keys(pattern: str = "*"):
    keys = rd.keys(pattern)
    return {"keys": keys}

@router.delete("/flush")
def flush_redis():
    rd.flushdb()
    return {"status": "all keys deleted"}