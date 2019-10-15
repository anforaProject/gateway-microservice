from fastapi import FastAPI
from v1.users import users

app = FastAPI()

app.include_router(
    users.router,
    prefix='/api/v1'
)
