from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service

router = APIRouter(prefix="/users", tags=["users"])

#post
@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate) -> UserResponse:
    created_user = user_service.create_user(user)

    # if the user could not be created, raise an exception
    if created_user is None:
        raise HTTPException(status_code=400, detail="User could not be created")
    return created_user

#get all users
@router.get("/", response_model=list[UserResponse])
def get_users():
    return user_service.get_user()

#get user by id
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = user_service.find_user(user_id)

    # if the user is not found, raise an exception
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user