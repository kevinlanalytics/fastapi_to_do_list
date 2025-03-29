# Main API file
from typing import List

from fastapi import FastAPI, HTTPException

from database import todo_list
from schemas import TodoItem

app = FastAPI()

# Create a new task
@app.post("/todos/", response_model=TodoItem)
async def create_todo(todo: TodoItem):
    todo_list.append(todo)
    return todo

# Get all tasks
@app.get("/todos/", response_model=List[TodoItem])
async def get_todos():
    return todo_list

# Get a single task by ID
@app.get("/todos/{todo_id}", response_model=TodoItem)
async def get_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Update a task
@app.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: int, updated_todo: TodoItem):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Delete a task
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
