import random

def generate_bp():

    systolic = random.randint(90, 180)

    diastolic = random.randint(50, 110)

    if diastolic >= systolic:

        diastolic = systolic - random.randint(30, 50)

    return systolic, diastolic