from pydantic import BaseModel, Field
from datetime import datetime

class AirMeasurement(BaseModel):
    sensor_id: str
    pm25: float = Field(..., ge=0)
    pm10: float = Field(..., ge=0)
    temperature: float
    humidity: float
    timestamp: datetime
