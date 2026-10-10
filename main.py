from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello World"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"message": f"hello User {user_id}"}

@app.get("/users/{user_name}")
def read_user(user_name: str):
    return {"message": f"hello User {user_name}"}
