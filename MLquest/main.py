
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
from utils.evaluator import evaluate_submission
import shutil
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return '''
    <h1>Welcome to MLQuest 🧠</h1>
    <p>Upload your solution to start your ML Quest.</p>
    <form action="/submit" enctype="multipart/form-data" method="post">
        <input name="problem_id" type="text" placeholder="problem1" required />
        <input name="file" type="file" required />
        <button type="submit">Submit</button>
    </form>
    '''

@app.post("/submit")
async def submit(file: UploadFile, problem_id: str = Form(...)):
    submission_path = f"submissions/{file.filename}"
    with open(submission_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = evaluate_submission(problem_id, submission_path)
    return {"result": result}
