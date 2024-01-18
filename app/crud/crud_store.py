from models.store import Goods, Owner
from schemas.store import OwnerCreate, GoodsCreate
from sqlalchemy.orm import Session



def create_owner(db: Session, obj_in: OwnerCreate) -> Owner:
    db_obj = Owner(
        name = obj_in.name,
        contact_info = obj_in.contact_info
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    return db_obj


def create_goods(db: Session, owner_id: int, obj_in: GoodsCreate):
    db_obj = Goods(**obj_in.model_dump(), owner_id=owner_id )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    return db_obj


def goods_for_owner(db: Session, owner_id: int):
    data = db.query(Goods).filter(Goods.owner_id == owner_id).all()
    return data


def owners_with_goods(db: Session):
    data = db.query(Owner).all()
    
    return data
