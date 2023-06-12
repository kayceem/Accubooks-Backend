from pydantic import BaseModel, ValidationError

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    passwd:str
    
class UserResponse(UserBase):
    id:int
    class Config:
        orm_mode = True