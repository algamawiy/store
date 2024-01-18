from sqlalchemy import (
    Column, Integer, String, ForeignKey, Enum
)
from sqlalchemy.orm import relationship
from db.database import Base
from enum import Enum as PyEnum


class Status(str, PyEnum):
    in_store = 'in_store'
    delivered = 'delivered'


class Owner(Base):
    __tablename__ = 'owners'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact_info = Column(String)

    goods = relationship("Goods", back_populates='owner')

class Goods(Base):
    __tablename__ = 'goods'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer, default=0)
    delivery_status = Column(Enum(Status))
    owner_id = Column(Integer, ForeignKey('owners.id'))
    
    owner = relationship("Owner", back_populates='goods')
    