from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

todos=[]

class Todo(BaseModel):
    id: int
    title:str
    completed:bool

#crud operation ka url simple rakhain gain 
#CREATAPI
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"messages":"Todo added","data":todo}


#GETAPI 
#but it will get the complelete dat that exist
@app.get("/todos")
def get_todos():
    return{todos}


#get api to access only the data we want
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"data": todo}
    return {"message": "Todo not found"}


# UPDATE API 
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {"message": "Todo updated", "data": updated_todo}
    return {"message": "Todo not found"}

# DELETE API
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            #or todos.pop
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}
