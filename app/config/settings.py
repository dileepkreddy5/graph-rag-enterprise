from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AWS_REGION: str
    BEDROCK_MODEL: str
    NEPTUNE_ENDPOINT: str

    model_config = {"env_file": ".env"}


settings = Settings()
