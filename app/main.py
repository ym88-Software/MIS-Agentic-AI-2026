from fastapi import FastAPI 
from app.Routes.TicketRoutes import router

app =FastAPI(title="Ticket routes in main")

app.include_router(router)

