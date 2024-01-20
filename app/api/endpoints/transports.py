from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from schemas.transport import (
    CarOwnerCreate, DriverCreate
)
from crud.crud_transport import (
    create_car_owner, create_driver
)



router = APIRouter()


@router.post('/add-car-owner')
def add_car_owner(obj_in: CarOwnerCreate, db: Session = Depends(get_db)):
    return create_car_owner(db=db, obj_in=obj_in)



@router.post('/add-driver')
def add_driver(obj_in: DriverCreate, db: Session = Depends(get_db)):
    return create_driver(db=db, obj_in=obj_in)
