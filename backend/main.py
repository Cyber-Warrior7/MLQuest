import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import problems, run, submit

app = FastAPI()

# 1) Health check root
@app.get("/", include_in_schema=False)
def root():
    return {"status": "ok"}

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(problems.router, prefix="/problems", tags=["problems"])
app.include_router(run.router,       prefix="/run",      tags=["run"])
app.include_router(submit.router,    prefix="/submit",   tags=["submit"])


if __name__ == "__main__":
    import uvicorn

    # 2) Read PORT from env and bind to all interfaces
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
    )
