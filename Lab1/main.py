#list of dictionary: our data
tickets= [
    {
        "id": 101,
        "customer": "Ahmed",
        "message": "My payment failed",
        "urgent": True,
    },
    {
        "id": 102,
        "customer": "Sara",
        "message": "I cannot login",
        "urgent": False,
    },
    {
        "id": 103,
        "customer": "Omar",
        "message": "Where is my order?",
        "urgent": False,
    },
    {
        "id": 104,
        "customer": "Ali",
        "message": "why my order late?",
        "urgent": True,
    },
]

#the data now is list of dictionary :
# next week will use pydantic => class and data validation , objects

# Ticket Classification Function in python logic
def classify_ticket(message :str)-> str :
    text = message.lower()
    if "payment" in text or "invoice" in text:
        return "billing"
    if "login" in text or "error" in text:
        return "technical"
    else:
        return "general"
    
""" category = classify_ticket("my payment failed")
print(category) """


# 10. Priority Function
def detect_priority(urgent:bool)->str:
    if urgent:
        return "high"
    return "normal"

""" piority = detect_priority(True)
print(piority) """


# Process One Ticket
def process_ticket(ticket:dict)->dict:

    category =classify_ticket(ticket["message"])
    priority = detect_priority(ticket["urgent"])
    #return Ticket_Result ->dict 
    return{
        "ticket_id":ticket["id"],
        "customer name":ticket["customer"],
        "category": category,
        "priority": priority,
    }


list_of_processed_tickets = [] #has all the Ticket_Result in dictionary format

for ticket in tickets:
    list_of_processed_tickets.append(process_ticket(ticket))
    dictionary1 = process_ticket(ticket)
    print(dictionary1)

counts ={
    "billing":0,
    "technical":0,
    "general":0
}

for ticket in tickets:
    category =classify_ticket(ticket["message"])
    counts[category]+=1
print(counts) 

#all things 
for ticket in tickets:
    print(process_ticket(ticket))

#our data in dictionary:
#next week  will be in objects and will use pydantic 
# we implement the functions 

def get_oreder(ticket_id :int)->dict:
    return{
        "status":"shipped",
        "avlue":"340"
    }
