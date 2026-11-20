from fastapi import FastAPI 
from enum import Enum

app = FastAPI()

@app.get("/")
async def home():
    return {"message" :"hello world"}

@app.post("/", description="this is end point post")
async def post():
    return {"message" :"this is post"}

#search on dynaic data
@app.get("/users/{user_id}")
async def get_user(user_id):
    return {"user id ": user_id}

#post , get , put , delete => endpoints inside the app (instance of API)

@app.put("/put")
async def put_mehod():
    return {"message" : " hello from put"}

#this is @ decorator 
@app.delete("/del")
async def delete_method():
    return {"message":"hello from delete"}


# 172.0.0.1:8000/docs => like postman to test endpoints 


#path parameter , static should be first , enums

class User_type(str , Enum):
    admin =1
    manager =2
    user =3

@app.get("/{users_type}/{user_id}")
async def get_user_type(users_type : User_type ,user_id):
    return {"users": users_type.name}

