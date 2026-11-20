from pydantic import BaseModel 
from typing import Literal

#literal =[list of output or list of input]
#input model + output mpdel 
class TicketResult(BaseModel):
    #the output will be one of them not any output structured output
    category : Literal["billing" ,"tech" ,"general"]
    priority :Literal["high" , "normal"]