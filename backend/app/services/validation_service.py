def validate_measurement(data) -> bool:
    if data.pm25 < 0 or data.pm10 < 0:
        return False
    if not (0 <= data.humidity <= 100):
        return False
    if not (-50 <= data.temperature <= 60):
        return False
    return True
