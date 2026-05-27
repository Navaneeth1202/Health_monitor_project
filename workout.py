from alarm import workout_alarm

# =========================================================
# WORKOUT CONFIRMATION
# =========================================================

def workout_confirmation():

    print("\n🏃 HIGH HEART RATE DURING ACTIVITY")

    workout_alarm()

    response = input(
        "\nPress D to confirm workout: "
    )

    if response.upper() == "D":

        print("\n✅ WORKOUT CONFIRMED")