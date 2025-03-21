from pydantic import BaseModel

class ListResponse(BaseModel):
    objects: list