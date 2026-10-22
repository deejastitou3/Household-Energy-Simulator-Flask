import random

def generer_consommation():
    """Generates a realistic 24-hour power consumption profile (in Watts)."""
    puissances = []
    for heure in range(24):
        if 0 <= heure < 6:
            p = random.randint(150, 300)      # Night: fridge, standby
        elif 6 <= heure < 9:
            p = random.randint(700, 1100)     # Morning: breakfast, showers
        elif 9 <= heure < 17:
            p = random.randint(350, 750)      # Day: low usage
        elif 17 <= heure < 22:
            p = random.randint(1600, 2600)    # Evening: cooking, TV, lights
        else:
            p = random.randint(450, 850)      # Late night
        puissances.append(p)
    return puissances