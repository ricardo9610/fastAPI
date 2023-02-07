#Python
from uuid import UUID
from datetime import date
from typing import Optional,List
from datetime import datetime

#pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


#FastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

#Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class Userlogin(UserBase):
    password: str = Field (
        ...,
        min_length=8,
        max_length= 64
    )

class User(UserBase):
    
    first_name: str = Field(
        ...,
        min_length = 1,
        max_length = 50
    )
    last_name: str = Field(
        ...,
        min_length = 1,
        max_length = 50
        
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    post: datetime = Field(default=datetime.now())
    update: Optional[datetime] = Field(default=None)
    by: User = Field(
        ...
    )

# Path Operations

@app.get(
    path= "/"
    )
def home():
    return {"Twitter API": "Working!"}

##  Users

@app.post(
    path="/sigingup",
    response_model= User,
    status_code= status.HTTP_201_CREATED,
    summary="Register user",
    tags=["Users"]
)
def sigingup():
    pass

@app.post(
    path="/login",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary= "login a user",
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="show all users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="show a user",
    tags=["Users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="delete a user",
    tags=["Users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="update a user",
    tags=["Users"]
)
def update_a_user():
    pass

## Tweets 