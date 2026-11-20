from pydantic import BaseModel, Field
from typing import Literal


class Ticket(BaseModel):
    id: int = Field(gt=0)
    customer_name: str = Field(min_length=3)
    message: str = Field(min_length=5)
    urgent: bool = False

class Ticket_Result(BaseModel):
    category: Literal["billing", "tech", "general"]
    priority: Literal["high", "normal"]


