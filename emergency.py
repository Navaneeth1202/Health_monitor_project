import threading
import time

import alarm

from sms_alert import send_sms

from config import (
    primary_contact,
    ambulance_number
)

# =========================================================
# CALL AMBULANCE
# =========================================================

def call_ambulance():

    print(
        f"\n🚑 CALLING AMBULANCE ({ambulance_number})..."
    )

# =========================================================
# EMERGENCY SOS
# =========================================================

def emergency_sos():

    alarm.sos_acknowledged = False

    # START BEEP

    alarm_thread = threading.Thread(
        target=alarm.beep_alarm
    )

    alarm_thread.daemon = True

    alarm_thread.start()

    # SEND SMS

    send_sms(primary_contact)

    # WAIT FOR RESPONSE

    start_time = time.time()

    while time.time() - start_time < 120:

        response = input(
            "\n🚨 Press D to stop emergency alert: "
        )

        if response.upper() == "D":

            alarm.sos_acknowledged = True

            print(
                "\n✅ EMERGENCY ALERT STOPPED"
            )

            return

    # NO RESPONSE

    alarm.sos_acknowledged = True

    print(
        "\n🚑 NO RESPONSE FOR 2 MINUTES"
    )

    call_ambulance()