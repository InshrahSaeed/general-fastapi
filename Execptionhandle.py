from fastapi import FastAPI,HTTPException

app = FastAPI()

class usernotfound(Exception):
    def __init__(self,name:str):
        self.name=name

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "name": "John Doe", "age": 30}