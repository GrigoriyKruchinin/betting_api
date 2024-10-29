from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_host: str
    app_port: int
    database_url: str
    line_provider_url: str

    class ConfigDict:
        env_file = ".env"


settings = Settings()
