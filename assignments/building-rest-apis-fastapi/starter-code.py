from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False


# TODO: Create an in-memory list of tasks
# TODO: Add a health check endpoint
# TODO: Add endpoints for creating, reading, updating, and deleting tasks
# TODO: Validate request data and return clear JSON responses


@app.get("/health")
def health_check():
    return {"status": "ok"}
