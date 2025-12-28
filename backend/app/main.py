from fastapi import FastAPI

app = FastAPI(
    title="AirChain API",
    description="Vertical prototype for air quality data validation on blockchain",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "service": "AirChain",
        "status": "running"
    }
