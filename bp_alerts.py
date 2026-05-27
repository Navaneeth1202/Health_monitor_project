import threading

from alarm import (
    low_bp_alarm,
    high_bp_alarm
)

from emergency import emergency_sos

# =========================================================
# INPUT WITH TIMEOUT
# =========================================================

def timed_input(prompt, timeout=10):

    user_input = [None]

    def get_input():

        user_input[0] = input(prompt)

    thread = threading.Thread(target=get_input)

    thread.daemon = True

    thread.start()

    thread.join(timeout)

    return user_input[0]

# =========================================================
# LOW BP ALERT
# =========================================================

def low_bp_alert():

    print("\n⚠ LOW BP DETECTED ⚠")

    low_bp_alarm()

    response = timed_input(
        "\nPress D to confirm safe condition (10 sec): ",
        10
    )

    if response and response.upper() == "D":

        print("\n✅ SAFE CONDITION CONFIRMED")

        return

    print("\n⚠ No response detected...")

    response = timed_input(
        "\nPress D again to confirm safety (10 sec): ",
        10
    )

    if response and response.upper() == "D":

        print("\n✅ SAFE CONDITION CONFIRMED")

        return

    print("\n🚨 NO RESPONSE - EMERGENCY SOS ACTIVATED 🚨")

    emergency_sos()

# =========================================================
# HIGH BP ALERT
# =========================================================

def high_bp_alert():

    print("\n⚠ HIGH BP DETECTED ⚠")

    high_bp_alarm()

    response = timed_input(
        "\nPress D to confirm safe condition (10 sec): ",
        10
    )

    if response and response.upper() == "D":

        print("\n✅ SAFE CONDITION CONFIRMED")

        return

    print("\n⚠ No response detected...")

    response = timed_input(
        "\nPress D again to confirm safety (10 sec): ",
        10
    )

    if response and response.upper() == "D":

        print("\n✅ SAFE CONDITION CONFIRMED")

        return

    print("\n🚨 NO RESPONSE - EMERGENCY SOS ACTIVATED 🚨")

    emergency_sos()