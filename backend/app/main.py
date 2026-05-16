from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .orchestrator import run_arena

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    solution: str
    history: list
    round: int


@app.get("/start")
def start():
    return {
        "scenario": "You are a backend engineer. Your payment system is under heavy load with 10,000 users. Ensure no duplicate transactions and fast response.",
        "round": 1
    }


@app.post("/submit")
def submit(data: UserInput):
    result = run_arena(data.solution, data.history, data.round)

    return {
        "attack": result["attack"],
        "edge_cases": result["edge_cases"],
        "feedback": result["feedback"],
        "score": result["score"],
        "round": data.round + 1
    }