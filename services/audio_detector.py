"""
Audio detection module.

This service decides if the detected scream is long enough
to be considered a distress signal.
"""

from app.config import SCREAM_DURATION_THRESHOLD


def detect_scream(scream_duration: float) -> bool:
    """
    Returns True if scream duration exceeds threshold.

    Parameters
    ----------
    scream_duration : float
        Duration of detected scream in seconds

    Returns
    -------
    bool
        True if scream considered distress signal
    """

    # Check scream duration
    if scream_duration >= SCREAM_DURATION_THRESHOLD:
        return True

    return False


# FUTURE IMPROVEMENT:
# Instead of duration only, integrate a scream classifier
# from Hugging Face or audio ML model.