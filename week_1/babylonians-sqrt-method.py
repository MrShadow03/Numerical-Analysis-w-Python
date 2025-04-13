def babylonian_sqrt_method(n, tolerance=1e-10):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")
    if n == 0:
        print("The square root of 0 is 0.")
        return 0

    guess = n / 2.0
    i = 0
    while True:
        print(f"Iteration {i}: guess = {guess}")
        next_guess = (guess + n / guess) / 2.0
        if abs(next_guess - guess) < tolerance:
            break
        guess = next_guess
        i += 1

    return guess

babylonian_sqrt_method(1)