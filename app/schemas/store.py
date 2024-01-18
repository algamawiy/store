from pydantic import BaseModel
from enum import Enum


class Status(str, Enum):
    
    in_sotre = 'in_store'
    delivered = 'delivered'


# Shared properties
class GoodsBase(BaseModel):
    name: str
    quantity: int
    delivery_status: Status
    
    
    
# Properties to receive via API on creation      
class GoodsCreate(GoodsBase):
    pass

# Properties to return via API
class Goods(GoodsBase):
    
    class Config:
        from_attributes = True


# Shared properties
class OwnerBase(BaseModel):
    name: str
    contact_info: str
    
    
    
# Properties to receive via API on creation      
class OwnerCreate(OwnerBase):
    pass
class Test(BaseModel):
    id: int = 0
    name: str = 'test'
    
    
# Properties to return via API
class Owner(OwnerBase):
    
    goods: list[Goods]
    class Config:
        from_attributes = True
        
        
