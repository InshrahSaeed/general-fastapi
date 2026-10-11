from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

#Put /users/101?notify=true
users=[]

class User(BaseModel):
    id:int
    age:int
    name:str


@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "user created", "data": user}


@app.post("/users/{user_id}")
def update_user(user_id: int, user: User, notify: bool = False):
    for u in users:
        if u.id == user_id:
            u.age = user.age
            u.name = user.name
            return {"message": "user updated", "data": u, "notify": notify}
    return {"message": "user not found"}