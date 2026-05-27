from config import (
    client,
    twilio_number
)

# =========================================================
# SEND SMS
# =========================================================

def send_sms(number):

    try:

        client.messages.create(

            body="🚨 MEDICAL EMERGENCY 🚨",

            from_=twilio_number,

            to=number
        )

        print("\n📩 MEDICAL EMERGENCY SMS SENT")

    except Exception as e:

        print("\n❌ SMS FAILED")

        print(e)