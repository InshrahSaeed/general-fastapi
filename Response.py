from fastapi import FastAPI
from pydantic import BaseModel  

app = FastAPI() 
#backend main hum user ka password store kar rahy hain lekin frontend main hum user ka password nahi dikhana chah rahy. is liye hum response model use kar rahy hain.To hide sensitive data like password from the response.


#request model: client se jo data ayega os ko hum request model main define kar rahy hain.
class User(BaseModel):
    id: int
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    age: int


#response model: client ko jo data send karna hain os ko hum response model main define kar rahy hain.
@app.get("/users", response_model=UserResponse)
def get_user():
    return {"id": 1, "name": "John Doe", "age": 30, "password":"1234"}  #ab response jo humain ui main milly ga os main password nahi ayega. password hide ho jyga.

