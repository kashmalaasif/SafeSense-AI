"""
Motion detection module.

Detects sudden violent jerk using accelerometer data.
"""

from app.config import JERK_THRESHOLD


def detect_jerk(acceleration: float) -> bool:
    """
    Detect sudden jerk movement.

    acceleration = magnitude of accelerometer spike

    Returns True if jerk detected
    """

    if acceleration >= JERK_THRESHOLD:
        return True

    return False


# FUTURE IMPROVEMENT:
# Use time-series anomaly detection on accelerometer data
# instead of single value.