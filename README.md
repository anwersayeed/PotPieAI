# PotPieAI

# Activate venv
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Docker - Run Redis container
docker run -d --name redis -p 6379:6379 redis
docker ps

# Run
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000