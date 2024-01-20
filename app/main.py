from fastapi import FastAPI
from api.endpoints import stores
from models import store
from db.database import engine



app = FastAPI()

store.Base.metadata.create_all(bind=engine)

app.include_router(stores.router)