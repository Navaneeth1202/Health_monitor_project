import random

def detect_motion(bp_sys, bp_dia, heart_rate):

    if (
        (
            (bp_sys < 90 or bp_dia < 60)
            or
            (bp_sys > 140 or bp_dia > 90)
        )
        and heart_rate > 130
    ):

        return "FALL"

    elif heart_rate > 120:

        return random.choice([
            "RUNNING",
            "WORKOUT"
        ])

    else:

        return random.choice([
            "RESTING",
            "WALKING"
        ])