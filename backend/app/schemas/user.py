from pydantic import BaseModel

#what we want to receive from the user when they sign up
class UserCreate(BaseModel):
    email: str
    name: str
    age: int

#what the user will receive when they sign up, we will use the same fields as UserBase but we will also add the id field
class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    age: int

    class Config:
        from_attributes = True #required to convert from SQLAlchemy model to Pydantic model