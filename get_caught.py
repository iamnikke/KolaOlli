import random

def get_caught():
    number = random.randint(0,100)
    if number > 70:
        return True
    else:
        return False

