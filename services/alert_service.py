"""
Alert system.

For hackathon prototype we simply print alerts.

Later you can integrate:

- SMS API
- WhatsApp API
- Email service
"""

from app.config import TRUSTED_CONTACTS


def send_alert(latitude, longitude):
    """
    Send emergency alert to trusted contacts.
    """

    location_link = f"https://maps.google.com/?q={latitude},{longitude}"

    for contact in TRUSTED_CONTACTS:

        print("🚨 EMERGENCY ALERT")
        print(f"Sending alert to {contact}")
        print("User might be in danger.")
        print(f"Location: {location_link}")
        print("----------------------")


# FUTURE IMPROVEMENT:
# Integrate Twilio or SMS gateway for real alerts.