from pydantic import BaseModel

class GuestbookEntry(BaseModel):
    id: int
    name: str
    message: str
    timestamp: str