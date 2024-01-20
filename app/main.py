from fastapi import FastAPI
from api.endpoints import stores, transports
from models import store, transport
from db.database import engine



#create database tables
store.Base.metadata.create_all(bind=engine)
transport.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(stores.router)
app.include_router(transports.router)