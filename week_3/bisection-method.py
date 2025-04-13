def bisection(f, a, b, tol=1e-10):
    """
    Bisection method for finding roots of a function.
    
    Parameters:
    f : function
        The function for which we are trying to find a root.
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    tol : float
        The tolerance for convergence.
        
    Returns:
    float
        An approximation of the root.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have different signs")
    
    while b - a > tol:
        midpoint = (a + b) / 2.0
        print(f"Current interval: [{a}, {b}], midpoint: {midpoint}, f({midpoint}) = {f(midpoint)}")
        if f(midpoint) == 0:
            return midpoint  # Found exact root
        elif f(a) * f(midpoint) < 0:
            b = midpoint  # Root is in left half
        else:
            a = midpoint  # Root is in right half

    
    return (a + b) / 2.0

# Example usage
f = lambda x: x**2 - 4
root = bisection(f, 1, 4)
print(f"Approximate root: {root:.6f}")