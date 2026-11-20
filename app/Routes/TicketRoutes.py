from fastapi import  APIRouter
from Schemas.TicketResult import TicketResult
from Schemas.Ticket import Ticket
from Services.classify_ticket import classify_ticket

router = APIRouter()

#app= FastAPI(title="tickets routes")

@router.get("/")
def home()->dict[str, str]:
    return {"message" : "ticket route get is working"}

@router.post("/tickets/classify",response_model=TicketResult)
def classify_ticket_route(ticket:Ticket)->TicketResult:
    return classify_ticket(ticket=ticket)
