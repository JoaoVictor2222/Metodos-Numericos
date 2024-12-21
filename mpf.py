import math

def fixed_point_iteration(g, x0, tolerance, max_iterations):
    """
    Performs fixed-point iteration to approximate the root of g(x) = x.

    Args:
        g: Function representing the fixed-point equation g(x) = x.
        x0: Initial guess.
        tolerance: Desired tolerance for convergence.
        max_iterations: Maximum number of iterations to perform.

    Returns:
        Approximation of the root or None if the method did not converge.
    """
    x = x0
    for iteration in range(max_iterations):
        x_next = g(x)

        if abs(x_next - x) < tolerance:
            return x_next

        x = x_next

    return None


def g(x):
    """
    Defines the function g(x) for the fixed-point equation g(x) = x.
    """
    return math.cos(x) ** 3

# Initial guess
x0 = 1.0

# Tolerance for convergence
tolerance = 1e-6

# Maximum number of iterations
max_iterations = 100

# Perform fixed-point iteration
approximation = fixed_point_iteration(g, x0, tolerance, max_iterations)

if approximation is not None:
    print("Approximation of the root:", approximation)
else:
    print("The method did not converge within the given number of iterations.")
