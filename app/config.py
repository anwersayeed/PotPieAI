from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Redis App"
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000

    redis_host: str
    redis_port: int
    redis_db: int
    redis_password: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()