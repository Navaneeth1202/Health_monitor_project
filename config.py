import os

from twilio.rest import Client

from dotenv import load_dotenv

# =========================================================
# LOAD ENV
# =========================================================

load_dotenv()

# =========================================================
# TWILIO CONFIG
# =========================================================

account_sid = os.getenv("ACCOUNT_SID")

auth_token = os.getenv("AUTH_TOKEN")

twilio_number = os.getenv("TWILIO_NUMBER")

client = Client(
    account_sid,
    auth_token
)

# =========================================================
# CONTACTS
# =========================================================

primary_contact = os.getenv(
    "PRIMARY_CONTACT"
)

ambulance_number = os.getenv(
    "AMBULANCE_NUMBER"
)

# =========================================================
# EXCEL FILE
# =========================================================

excel_file = "health_monitor_data.xlsx"