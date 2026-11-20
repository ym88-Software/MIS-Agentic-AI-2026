from app.Schemas.Ticket import Ticket
from app.Schemas.TicketResult import TicketResult


def classify_ticket(ticket :Ticket)->TicketResult:
    text = ticket.message.lower()

    category =""
    if "payment" in text or "invoice" in text:
        category ="billing"
    elif "login"in text or "error" in text:
        category = "tech"
    else:
        category ="general"

    priority = "high" if ticket.urgent else "normal"

    return TicketResult(category=category , priority=priority)
