"""
Load environment variables and validation of project configurations from user
"""
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from .tetue_generic.generic_requests import GenReqConfiguration
from .db import DbConfiguration

load_dotenv("files/.env")


class Configuration(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='TT_', env_nested_delimiter='__')

    user: str
    vorname: str = "JoJo"
    gen_req: GenReqConfiguration
    db: DbConfiguration
