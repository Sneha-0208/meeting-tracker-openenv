from pydantic import BaseModel
from typing import List, Optional

class TaskItem(BaseModel):
    description: str
    owner: Optional[str] = None
    deadline: Optional[str] = None
    priority: Optional[str] = None


class Observation(BaseModel):
    transcript: str
    tasks: List[TaskItem]
    step: int
    remaining_steps: int


class Action(BaseModel):
    action_type: str
    description: Optional[str] = None
    owner: Optional[str] = None
    deadline: Optional[str] = None
    priority: Optional[str] = None