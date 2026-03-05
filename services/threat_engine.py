"""
Threat decision engine.

This is the core logic of the system.

Alert rule defined by you:

1 violent jerk movement + scream lasting >=10 seconds
"""

from app.services.audio_detector import detect_scream
from app.services.motion_detector import detect_jerk


def evaluate_threat(scream_duration, acceleration):
    """
    Combine scream detection and motion detection.

    Returns a threat score.
    """

    risk_score = 0

    # Detect scream
    scream_detected = detect_scream(scream_duration)

    # Detect violent jerk
    jerk_detected = detect_jerk(acceleration)

    if scream_detected:
        risk_score += 40

    if jerk_detected:
        risk_score += 40

    # Final decision logic
    threat = False

    if scream_detected and jerk_detected:
        threat = True

    return {
        "threat": threat,
        "risk_score": risk_score
    }


# FUTURE IMPROVEMENT:
# Add additional signals:
# - distress speech detection
# - repeated jerks
# - location risk