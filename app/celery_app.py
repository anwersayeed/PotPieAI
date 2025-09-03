from celery import Celery
from app.config import settings

celery = Celery(
    "worker",
    broker=f"redis://{settings.redis_host}:{settings.redis_port}/{settings.redis_db}",
    backend=f"redis://{settings.redis_host}:{settings.redis_port}/{settings.redis_db}"
)

celery.autodiscover_tasks(["app"])