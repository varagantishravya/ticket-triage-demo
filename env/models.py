from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    ticket_id: int
    message: str
    customer_type: str

class Action(BaseModel):
    category: str   # billing / technical / general
    priority: str   # low / medium / high
    response: str

class Reward(BaseModel):
    score: float
    feedback: Optional[str]