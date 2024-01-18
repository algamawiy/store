from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from api.deps import get_db
from schemas.store import GoodsCreate, OwnerCreate, Owner
from crud.crud_store import create_goods, create_owner, goods_for_owner, owners_with_goods


router = APIRouter(
    prefix='/stores',
    tags=['Stores']
)


@router.post('/add-owner')
def add_goods_owner(owner: OwnerCreate, db: Session = Depends(get_db)):
    return create_owner(db=db, obj_in=owner)


@router.post('/add-goods/{id}')
def add_goods(goods: GoodsCreate, id: int, db: Session = Depends(get_db)):
    return create_goods(db=db, owner_id=id, obj_in=goods)


@router.get('/goods/{id}')
def owners_goods(id: int, db: Session = Depends(get_db)):
    return goods_for_owner(db=db, owner_id=id)


@router.get('/owners-with-goods', response_model=list[Owner])
def read_owners_with_goods(db: Session = Depends(get_db)):
    return owners_with_goods(db=db)