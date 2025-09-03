# PotPieAI

# Activate venv
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Store in postgres, Redis for Cache
# Redis - In memory - means RAM
# Docker - Run Redis container - TTL can be set - as stores in RAM and huge data cannot be stored - no joins, and not reliable
docker run -d --name redis -p 6379:6379 redis
docker ps

# Run
# uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
.\venv\Scripts\Activate
uvicorn main:app --reload

# Separately run Celery
# celery -A app.celery_app.celery worker --loglevel=info
.\venv\Scripts\Activate
celery -A app.celery_app.celery worker --loglevel=info --pool=solo
- Start Task:- (calls routers->github.py->analyze_latest_pr) http://127.0.0.1:8000/github/latest-pr/analyze
- Task Status:- GET http://127.0.0.1:8000/github/task/{task_id}