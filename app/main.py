"""
Entry point of the backend server.
"""

from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Goose Women's Safety Backend"
)

# Register routes
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Safety Backend Running"}