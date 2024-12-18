"""
    temp file
"""
from pydantic import BaseModel

class DbConfiguration(BaseModel):
    """
    Configuration settings for database handler
    """
    ip: str
    user: str
    active: bool = True
