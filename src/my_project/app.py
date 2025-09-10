from fastapi import FastAPI

from my_project.api.routes import router

app = FastAPI()

async def lifespan(app: FastAPI):
    """
    Acquire and close application-wide resources.
    """
    yield app


@app.get("/startup")
async def startup_probe():
    return {"status": "ok"}

@app.get("/liveness")
async def liveness_probe():
    return {"status": "alive"}

@app.get("/readiness")
async def readiness_probe():
    return {"status": "ready"}


app.include_router(router)
