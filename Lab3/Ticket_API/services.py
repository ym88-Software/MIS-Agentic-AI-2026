from .models import Ticket, Ticket_Result

def classify_ticket(ticket: Ticket) -> Ticket_Result:
    text = ticket.message.lower()

    category = ""
    if "payment" in text or "invoice" in text:
        category = "billing"
    elif "login" in text or "error" in text:
        category = "tech"
    else:
        category = "general"

    priority = "high" if ticket.urgent else "normal"

    return Ticket_Result(category=category, priority=priority)
