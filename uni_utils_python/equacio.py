from math import sqrt

def equacio(a: float, b: float, c: float) -> tuple:
    """
    Retorna el número d'arrels i les dues arrels (codi, arrel1, arrel2)
    introduint els coeficients de la forma ax^2 + bx + c.

    Args:
        a (float): Coeficient de x^2.
        b (float): Coeficient de x.
        c (float): Termini independent.

    Returns:
        tuple: Un tuple amb el número d'arrels i les dues arrels (arrel1, arrel2).
               Retorna (0, None, None) si no hi ha arrels, 
               (1, arrel1, None) si hi ha una sola arrel, 
               o (2, arrel1, arrel2) si hi ha dues arrels.
    """
    sqrt_input = (b**2) - (4*a*c)

    if sqrt_input < 0:
        return 0, None, None
    elif sqrt_input == 0:
        arrel1 = -b / (2*a)
        return 1, arrel1, None
    else:
        arrel1 = (-b + sqrt(sqrt_input)) / (2.0*a)
        arrel2 = (-b - sqrt(sqrt_input)) / (2.0*a)
        return 2, arrel1, arrel2
