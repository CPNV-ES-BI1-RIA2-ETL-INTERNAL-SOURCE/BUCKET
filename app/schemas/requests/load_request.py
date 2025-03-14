from pydantic import BaseModel

class LoadRequest(BaseModel):
    data: str
    uri: str
