from sqlalchemy.orm import Session
from models.transport import (
    GoodsOwner, CarOwner, Trip, Receipt, Driver
)
from schemas.transport import (
    CarOwnerCreate, TripCreate, DriverCreate, ReceiptsCreate
)



def create_car_owner(db: Session, obj_in: CarOwnerCreate):
    db_obj = CarOwner(
        full_name = obj_in.full_name
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    return db_obj



def create_driver(db: Session, obj_in: DriverCreate):
    db_obj = Driver(
        full_name = obj_in.full_name
        
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    return db_obj



