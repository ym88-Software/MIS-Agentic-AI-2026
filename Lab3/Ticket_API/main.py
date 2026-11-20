from .routes import router 

from fastapi import FastAPI


app = FastAPI(
    title="tickets Api ",
    description="lab 3",
    version="1.0.0"
)

app.include_router(router)
