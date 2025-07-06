from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import problems, run, submit

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(problems.router, prefix="/problems", tags=["problems"])
app.include_router(run.router, prefix="/run", tags=["run"])
app.include_router(submit.router, prefix="/submit", tags=["submit"])
