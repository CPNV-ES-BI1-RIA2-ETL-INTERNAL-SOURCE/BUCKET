from pydantic import BaseModel

class LoadResponse(BaseModel):
    url: str