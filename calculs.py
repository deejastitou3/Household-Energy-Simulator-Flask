import numpy as np

def calculer_energie(puissances):
    """Calculates total energy using the Trapezoidal Rule (np.trapezoid)."""
    try:
        # NumPy 2.0+ uses np.trapezoid
        E_Wh = np.trapezoid(puissances, dx=1) 
    except AttributeError:
        # Fallback for older NumPy versions
        E_Wh = np.trapz(puissances, dx=1)
        
    # Convert Wh to kWh and round to 2 decimal places
    return round(E_Wh / 1000, 2)