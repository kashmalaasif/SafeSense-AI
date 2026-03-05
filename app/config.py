"""
This file stores configuration values.

In production these values would come from environment variables.
"""

# Minimum scream duration required to trigger alert
SCREAM_DURATION_THRESHOLD = 10  # seconds

# Movement acceleration threshold for jerk detection
JERK_THRESHOLD = 18  # change this after testing

# Minimum risk score to trigger emergency alert
RISK_SCORE_THRESHOLD = 60

# Dummy emergency contacts for prototype
TRUSTED_CONTACTS = [
    "+123456789",
    "+987654321"
]