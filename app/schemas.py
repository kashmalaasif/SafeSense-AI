"""
Schemas define the structure of data received from the mobile app.

FastAPI automatically validates incoming JSON using these models.
"""

from pydantic import BaseModel


class SensorInput(BaseModel):
    """
    Data coming from the mobile application
    """

    scream_duration: float  # duration of scream in seconds
    acceleration: float     # accelerometer spike value
    latitude: float
    longitude: float