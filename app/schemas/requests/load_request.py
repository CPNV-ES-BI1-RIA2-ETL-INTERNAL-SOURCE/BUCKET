from pydantic import BaseModel

class LoadRequest(BaseModel):
    data: str
    destination: str