from fastapi import FastAPI
from app.config import settings
from app.routes import user

app = FastAPI(title=settings.app_name)

@app.get("/")
def root():
    return {"message": "Hello World!", "env": settings.app_env}

# Include user routes
app.include_router(user.router)