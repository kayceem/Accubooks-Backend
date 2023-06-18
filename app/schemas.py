from pydantic import BaseModel, ValidationError
from typing import Optional
from datetime import date

class User(BaseModel):
    name:Optional[str]
    username:str
    email: str
    contact_number:int
    password:str
    
class UserLogin(BaseModel):
    username:str
    password:str
    

class Product(BaseModel):
    name:str
    quantity:Optional[int]

class CreateTransaction(BaseModel):
    product_id:int
    quantity:int
    date:date
    price:int
    
class PurchaseCreate(CreateTransaction):
    pass

class SalesCreate(CreateTransaction):
    pass

class SalesUpdate(CreateTransaction):
    sales_id:int
    
class PurchaseUpdate(CreateTransaction):
    purchase_id:int

    