"""
    temp file
"""
from pydantic import BaseModel, IPvAnyAddress

class DbConfiguration(BaseModel):
    """
    Configuration settings for database handler
    """
    ip: IPvAnyAddress
    user: str
    active: bool = True

def helli():
    print("test lala")
