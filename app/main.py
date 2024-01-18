from fastapi import FastAPI
from api.endpoints import stores



app = FastAPI()

app.include_router(stores.router)