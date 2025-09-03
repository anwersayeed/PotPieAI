from fastapi import FastAPI
from app.routers import github

app = FastAPI(title="FastAPI GitHub PR App")

# Routers
app.include_router(github.router)

@app.get("/")
def root():
    return {"message": "GitHub PR API with Celery running!"}
