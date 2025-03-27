"""
Load environment variables and validation of project configurations from user
"""
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from .tetue_generic.generic_requests import GenReqConfiguration
from .tetue_generic.watcher import WatcherConfiguration

load_dotenv("default.env")
load_dotenv("files/.env", override=True)


class Configuration(BaseSettings):
    """
    Configuration class to merge all settings for the application and validate via pydantic

    Args:
        BaseSettings (BaseSettings): Base class for settings from environment variables.
    """
    model_config = SettingsConfigDict(env_prefix='TT_', env_nested_delimiter='__')

    gen_req: GenReqConfiguration
    watcher: WatcherConfiguration
