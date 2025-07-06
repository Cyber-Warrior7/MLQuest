from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

@router.get("/")
def list_problems():
    problems_dir = Path("backend/problems")
    problems = []
    for file in problems_dir.glob("*.json"):
        with open(file) as f:
            problems.append(json.load(f))
    return problems
