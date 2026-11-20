from pydantic import BaseModel, Field
from fastapi import FastAPI 
from typing import Literal

# we take an object from Fastabi
app =FastAPI(
    title="tickets Api ",
    description="lab 2",
    version="1.0.0"
)
# then the pydantic enforce the contract == data validation == reject bad input before problem begin
class  Ticket(BaseModel):
    customer_name :str    # each field has type
    message :str = Field(min_length=5)
    urgent :bool = False     #default value 

class TicketResult(BaseModel):
    #the output will be one of them not any output structured output
    category : Literal["billing" ,"tech" ,"general"]
    priority :Literal["high" , "normal"]


""" ticket1= Ticket(customer_name="youssef", message="my payment failed?" , urgent=True)
print(ticket1) """

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

#test
ticket_Youssef =Ticket(customer_name="youssef" ,message="i cannot login")
result :TicketResult = classify_ticket(ticket_Youssef)
print(result.model_dump_json())


