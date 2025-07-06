from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.utils.executor import execute_code

router = APIRouter()

class CodeRequest(BaseModel):
    code: str

@router.post("/cell")
def run_cell(payload: CodeRequest):
    try:
        output = execute_code(payload.code)
        return {"output": output}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
