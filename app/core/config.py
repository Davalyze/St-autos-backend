from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # ======================================
    # PostgreSQL (Base de datos ERP ST-AUTOS)
    # ======================================
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # ======================================
    # Seguridad / JWT
    # ======================================
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXP_HOURS: int = 12

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
