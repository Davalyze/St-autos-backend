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
    
    
    AZURE_STORAGE_ACCOUNT_NAME: str
    AZURE_STORAGE_ACCOUNT_KEY: str
    AZURE_STORAGE_CONTAINER: str
    AZURE_STORAGE_ENDPOINT_SUFFIX: str = "core.windows.net"
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
