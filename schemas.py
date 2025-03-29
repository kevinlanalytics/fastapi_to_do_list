# Request/response schemas
from typing import Optional

from pydantic import BaseModel


class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool = False
    