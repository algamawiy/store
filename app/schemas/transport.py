from pydantic import BaseModel
from enum import Enum


#Car Owner

# Shared properties
class CarOwnerBase(BaseModel):
    full_name: str
    
    
    
# Properties to receive via API on creation      
class CarOwnerCreate(CarOwnerBase):
    pass

# Properties to return via API
class CarOwner(CarOwnerBase):
    
    class Config:
        from_attributes = True
        
#Driver
class DriverBase(BaseModel):
    full_name: str
    
   
   
class DriverCreate(DriverBase):
    pass
      
 

class Driver(DriverBase):
    
    class Config:
        from_attributes = True
    


#Trip

# Shared properties
class TripBase(BaseModel):
    fromm: str
    to: str
    
    
    
# Properties to receive via API on creation      
class TripCreate(TripBase):
    driver_id: int

# Properties to return via API
class Trip(TripBase):
    
    class Config:
        from_attributes = True
        
  
#Receipts

class ReceiptsBase(BaseModel):
    driver_name: str
    address: str
    goods: str
    quantity: int
    #goods_owner_id: int
    #trip_id: int
    
    #goods_owner = relationship
    #trip = relationship 
    
    
class ReceiptsCreate(ReceiptsBase):
    
    goods_owner_id: int
    trip_id: int
    
    #goods_owner = relationship
    #trip = relationship 
  

class Receipts(ReceiptsBase):
    
    class Config:
        from_attributes = True
    

        

#Goods Owner

# Shared properties
class GoodsOwnerBase(BaseModel):
    full_name: str
    phone: str
    goods: str
    quantity: int
    
    
    
# Properties to receive via API on creation      
class GoodsOwnerCreate(GoodsOwnerBase):
    pass

# Properties to return via API
class GoodsOwner(GoodsOwnerBase):
    
    receipts: list[Receipts] | None = None
    class Config:
        from_attributes = True