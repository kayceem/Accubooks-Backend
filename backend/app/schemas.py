from pydantic import BaseModel, ValidationError
from typing import Optional
from datetime import date

class User(BaseModel):
    name:Optional[str]
    username:str
    email: str
    contact_number:int
    password:str

class Product(BaseModel):
    product_name:str
    id:int
    quantity:Optional[int]

class Purchase(BaseModel):
    product_id:int
    quantity:int
    date:date
    price:int

class Sales(BaseModel):
    product_id:int
    quantity:int
    date:date
    price:int

    