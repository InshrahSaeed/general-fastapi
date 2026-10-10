from pydantic import BaseModel,ConfigDict,Field
from fastapi import FastAPI

app = FastAPI()
#basemodel: base class that all of the models should inherit from
#configdict: used to configure the model's behavior
#field: used to define the fields of the model and their validation rules. let us add constraints to the fields of the model, such as minimum and maximum length, regex patterns, and default values.
class Post(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str = Field(min_length=3, max_length=100)
    content: str = Field( min_length=10)
    author: str = Field(..., min_length=1, max_length=50)


class PostCreate(Post):
    #pass means that the class does not have any additional attributes or methods beyond what is inherited from the Post class. It is used as a placeholder to indicate that the class is intentionally left empty and does not require any additional functionality.
    pass

class PostResponse(Post):
    model_config = ConfigDict(from_attributes=True)# from_attributes=True it tell pydantic that it can read data from an object with attributes and not just a dictionary
    id:int 
    date_posted:str

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/create-user")
def create_user(user: User):
 return {"message": "User created", "data": user}

#nested paydentic
class Address(BaseModel):
 city: str
 pincode: int
class User(BaseModel):
    name: str
    age: int
    address: Address # dono classes link ho gayi


@app.post("/create-user")
def create_user(user: User):
 return user # ab is user main address and user donon k attributes hon gain 
