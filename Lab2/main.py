from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal


app = FastAPI(
    title="tickets Api ",
    description="lab 2",    
    version="1.0.0"
)


class Ticket(BaseModel):
    id : int = Field(gt=0)
    customer_name: str = Field(min_length=3)
    message: str = Field(min_length=5)
    urgent: bool = False


class TicketResult(BaseModel):
    category: Literal["billing", "tech", "general"] 
    priority: Literal["high", "normal"]


def classify_ticket(ticket: Ticket) -> TicketResult:
    text = ticket.message.lower()

    category = ""
    if "payment" in text or "invoice" in text:
        category = "billing"
    elif "login" in text or "error" in text:
        category = "tech"
    else:
        category = "general"

    priority = "high" if ticket.urgent else "normal"

    return TicketResult(category=category, priority=priority)


@app.get("/")
def home():
    return {"message": "hello world"}



@app.post("/classify_ticket", response_model=TicketResult)
def classify_ticket_endpoint(ticket: Ticket):
    result = classify_ticket(ticket)
    return result   