from sqlalchemy import (
    Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import relationship
from db.database import Base
#from enum import Enum


   
class CarOwner(Base):
    __tablename__ = 'car_owners'
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    
    drivers = relationship("Driver", back_populates='car_owner')
    

  
class Driver(Base):
    __tablename__ = 'drivers'
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    car_owner_id = Column(Integer, ForeignKey('car_owners.id'))
    
    car_owner = relationship("CarOwner", back_populates='drivers')
    trips = relationship("Trip", back_populates='driver')

 

    
class Trip(Base):
    __tablename__ = 'trips'
    
    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    fromm = Column(String)
    to = Column(String)
    driver = relationship("Driver", back_populates='trips')
    receipts = relationship('Receipt', back_populates='trip')
    
    
    
    
class GoodsOwner(Base):
    __tablename__ = 'goods_owners'
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    phone = Column(String)
    goods = Column(String)
    quantity = Column(Integer, default=0)
    
    receipts = relationship('Receipt', back_populates='goods_owner')
    
    
class Receipt(Base):
    __tablename__ = 'receipts'
    
    id = Column(Integer, primary_key=True, index=True)
    driver_name = Column(String)
    address = Column(String)
    goods = Column(String)
    quantity = Column(Integer, default=0)
    goods_owner_id = Column(Integer, ForeignKey('goods_owners.id'))
    trip_id = Column(Integer, ForeignKey('trips.id'))
    
    goods_owner = relationship('GoodsOwner', back_populates='receipts')
    trip = relationship('Trip', back_populates='receipts')
    
    

