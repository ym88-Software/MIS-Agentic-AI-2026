from pydantic import BaseModel ,Field
from typing import Literal

class Ticket (BaseModel):
#add some constrain at the fields 
    customer_name :str  = Field(min_length=2)
    urgent :bool =False # has default value can not pass to object 
    message :str = Field(min_length=5 ,description="enter your message")



