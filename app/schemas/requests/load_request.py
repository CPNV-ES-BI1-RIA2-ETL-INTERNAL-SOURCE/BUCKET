from pydantic import BaseModel

class LoadRequest(BaseModel):
    file: str
    destination: str