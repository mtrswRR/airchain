from fastapi import FastAPI
from app.api.measurements import router as measurements_router

app = FastAPI(
    title="AirChain API",
    description="Vertical prototype for air quality data validation on blockchain",
    version="0.1.0"
)

app.include_router(measurements_router)

@app.get("/")
def root():
    return {"service": "AirChain", "status": "running"}
