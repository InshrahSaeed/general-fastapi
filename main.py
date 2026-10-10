from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "hello World"}


# @app.get("/users/{user_id}")
# def read_user(user_id: int ):
#     return {"message": f"hello User {user_id}"}


#single query parameter
@app.get("/users")
def read_users(name: str = None):
    return {"name": name}

#optional query parameter with default value
@app.get("/products")
def read_products(limit: int = 10):
    return {"limit": limit}


#multiple query parameters
@app.get("/items")
def read_item(name: str = None, price: int = 0):
    return {"name": name, "price": price}