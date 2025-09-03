from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    app_name: str = "FastAPI GitHub PR App"
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000

    # Redis
    redis_host: str
    redis_port: int
    redis_db: int

    # GitHub
    github_token: str
    github_repo: str

    class Config:
        env_file = ".env"

settings = Settings()