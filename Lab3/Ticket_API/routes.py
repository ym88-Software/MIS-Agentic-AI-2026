from fastapi import APIRouter

from .models import Ticket, TicketResult
from .services import classify_ticket

router = APIRouter()

@router.get("/")
def home():
    return {"message": "hello from cs415 "}

@router.post("/classify_ticket", response_model=TicketResult)
def classify_ticket_endpoint(ticket: Ticket)-> TicketResult:
    return classify_ticket(ticket) 

 


