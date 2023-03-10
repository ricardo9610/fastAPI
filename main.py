#Python
from uuid import UUID
from datetime import date
from typing import Optional,List
from datetime import datetime
import json

#pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

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

class UserRegister(User):
    password: str = Field (
        ...,
        min_length=8,
        max_length= 64
    )

class UserRegister(User):
    password: str = Field (
        ...,
        min_length=8,
        max_length= 64
    )

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(
        ...
    )

# Path Operations

##  Users

### Register a user
@app.post(
    path="/sigingup",
    response_model= User,
    status_code= status.HTTP_201_CREATED,
    summary="Register user",
    tags=["Users"]
)
def sigingup( user: UserRegister = Body(...)):
    """
    this path opetarion register a user in the app

    parameters:
        -Request body parameter
            - user: UserRegister

    Returns a json with the basic user information:
        - user_id: UUIDcd 
        - email: Emailstr
        - first name:str
        - last_name: str
        - birth_date: date
    """
    with open("users.json","r+",encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user 


### login a user
@app.post(
    path="/login",
    response_model= User,
    status_code=status.HTTP_200_OK,
    summary= "Login a user",
    tags=["Users"]
)
def login():
    pass

### show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    """ 
    this path operation show all users in the app 

    parameters:
        -

    returns a json list with all users in the app, with the following keys 
        - user_id: UUIDcd ..
        - email: Emailstr
        - first name:str
        - last_name: str
        - birth_date: date
    """

    with open ("users.json" ,"r", encoding= "utf-8") as f:
        results = json.loads(f.read())
        return results

### show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user():
    pass

### delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_a_user():
    pass

### update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
)
def update_a_user():
    pass

## Tweets 

### Show all tweets
@app.get(
    path= "/",
    response_model=List[Tweet],
    status_code= status.HTTP_201_CREATED,
    summary="Show all tweets",
    tags=["Tweets"]
    )
def home():
    """ 
    this path operation show all Tweets in the app 

    parameters:
        -

    returns a json list with all Tweets in the app, with the following keys 
        - tweet_id: UUID 
        - created_at: datetime 
        - updated_at: Optional[datetime]
        - by: User 
    """
    with open ("tweets.json" ,"r", encoding= "utf-8") as f:
        results = json.loads(f.read())
        return results

### Post a tweet
@app.post(
    path="/post",
    response_model= Tweet,
    status_code= status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post(tweet: Tweet = Body(...)):
    """
    post a tweet

    this path opetarion post a tweet in the app

    parameters:
        -Request body parameter
            - tweet: Tweet

    Returns a json with the basic tweet information:
        - tweet_id: UUIDcd ..
        - content: str
        - create_at:datetime
        - updated_at: datetime
        - by: User
    """
    with open("tweets.json","r+",encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])

        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model= Tweet,
    status_code= status.HTTP_201_CREATED,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model= Tweet,
    status_code= status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass