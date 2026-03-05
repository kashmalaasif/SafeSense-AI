"""
API routes.

Mobile app sends sensor data to this endpoint.
"""

from fastapi import APIRouter
from app.schemas import SensorInput
from app.services.threat_engine import evaluate_threat
from app.services.alert_service import send_alert

router = APIRouter()


@router.post("/sensor-data")
def process_sensor_data(data: SensorInput):
    """
    This endpoint receives sensor data from the mobile app.
    """

    # Step 1: evaluate threat
    result = evaluate_threat(
        data.scream_duration,
        data.acceleration
    )

    # Step 2: trigger alert if threat detected
    if result["threat"]:
        send_alert(data.latitude, data.longitude)

    return {
        "status": "processed",
        "threat_detected": result["threat"],
        "risk_score": result["risk_score"]
    }


# FUTURE IMPROVEMENT:
# Add logging database to store incidents.