from fastapi import FastAPI
#from lib import class 

from pydantic import BaseModel
#from lib import class :basemode : parent class : to define data type for vvariable 

class Student(BaseModel):
    name:str
    age :int


#how to declare and crete object 
student = Student(name="youssef",age=21)


app = FastAPI()#object
# app is object has all functions and prperites of FastAPI class


@app.get("/")
def home():
    return {"message": "Hello Youssef!"}


#client , provider , .env, congig , llm,