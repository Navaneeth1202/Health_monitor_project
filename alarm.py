import winsound
import time

# =========================================================
# GLOBAL FLAG
# =========================================================

sos_acknowledged = False

# =========================================================
# EMERGENCY CONTINUOUS ALARM
# =========================================================

def beep_alarm():

    global sos_acknowledged

    while sos_acknowledged == False:

        winsound.Beep(1500, 700)

        winsound.Beep(1000, 700)

# =========================================================
# LOW BP ALARM
# =========================================================

def low_bp_alarm():

    print("\n🔔 LOW BP WARNING ALARM 🔔")

    for i in range(8):

        winsound.Beep(900, 1000)

        time.sleep(0.2)

# =========================================================
# HIGH BP ALARM
# =========================================================

def high_bp_alarm():

    print("\n🔔 HIGH BP WARNING ALARM 🔔")

    for i in range(8):

        winsound.Beep(1400, 1000)

        time.sleep(0.2)

# =========================================================
# WORKOUT ALARM
# =========================================================

def workout_alarm():

    winsound.Beep(1200, 800)