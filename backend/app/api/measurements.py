from fastapi import APIRouter, HTTPException
from app.models.measurement import AirMeasurement
from app.services.validation_service import validate_measurement
from app.blockchain.blockchain_service import write_to_blockchain

router = APIRouter(prefix="/api/measurements", tags=["Measurements"])


@router.post("/")
def submit_measurement(measurement: AirMeasurement):
    if not validate_measurement(measurement):
        raise HTTPException(status_code=400, detail="Invalid measurement data")

    blockchain_result = write_to_blockchain(measurement)

    return {
        "message": "Measurement accepted",
        "blockchain": blockchain_result
    }
