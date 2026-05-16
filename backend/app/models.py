from pydantic import BaseModel

class UserInput(BaseModel):
    solution: str
    history: list
    round: int