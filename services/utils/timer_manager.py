"""
timer_manager.py

This module is responsible for managing the SCREAM TIMER.

Purpose:
---------
We only trigger an alert if a scream lasts for a certain duration.
This helps reduce FALSE POSITIVES such as:
- someone shouting normally
- loud background noise
- short accidental sounds

Example Logic:
---------------
If scream is detected:
    Start timer
If scream continues:
    keep counting time
If scream stops before threshold:
    reset timer
If scream exceeds threshold:
    return TRUE -> emergency trigger

This file will be used by the main backend pipeline.
"""

import time


class ScreamTimer:
    """
    This class tracks how long a scream lasts.
    """

    def __init__(self, threshold_seconds=10):
        """
        Constructor

        threshold_seconds:
        Minimum scream duration required to trigger alert.
        Example: 10 seconds scream -> emergency.
        """

        self.threshold = threshold_seconds
        self.start_time = None
        self.active = False

    def start(self):
        """
        Start the scream timer.
        This function should be called when scream is first detected.
        """

        if not self.active:
            self.start_time = time.time()
            self.active = True

    def reset(self):
        """
        Reset timer when scream stops.
        """

        self.start_time = None
        self.active = False

    def check_duration(self):
        """
        Check how long the scream has lasted.

        Returns:
        --------
        True  -> scream duration exceeded threshold
        False -> scream duration not long enough
        """

        if not self.active:
            return False

        elapsed_time = time.time() - self.start_time

        if elapsed_time >= self.threshold:
            return True

        return False