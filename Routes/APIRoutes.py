#WE CAN generate all routes in the main file but it will make the fill messy and hard to read. So we will create a separate file for the routes and import them in the main file.
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

# ab agr hum aik main application bna rahy hain to os main jahan bhi humain zyadah routes ki zarort hogi to apny code ko managable rakhny k liya hum har section ki laga file route file bna lain gain or project ki main file mian import kr lain gain 
    

todos=[]

class Todo(BaseModel):
    id: int
    title:str
    completed:bool

router = APIRouter()
@router.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"messages":"Todo added","data":todo}


#GETAPI 
#but it will get the complelete dat that exist
@router.get("/todos")
def get_todos():
    return{todos}


#get api to access only the data we want
@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"data": todo}
    return {"message": "Todo not found"}


# UPDATE API 
@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {"message": "Todo updated", "data": updated_todo}
    return {"message": "Todo not found"}

# DELETE API
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            #or todos.pop
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}
