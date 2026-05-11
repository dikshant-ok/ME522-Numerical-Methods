"""
root_finding.py
---------------
Numerical root-finding methods library for ME-522.
Implements Bisection, Newton-Raphson, and Secant methods.
"""


def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Bisection Method
    ----------------
    Finds root of f(x) = 0 in interval [a, b].
    Requires f(a) and f(b) to have opposite signs.

    Parameters:
        f        : callable, the function
        a, b     : float, interval endpoints
        tol      : float, tolerance for convergence
        max_iter : int, maximum iterations

    Returns:
        dict with root, iterations, error history
    """
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    errors = []
    for i in range(1, max_iter + 1):
        mid = (a + b) / 2.0
        err = abs(b - a) / 2.0
        errors.append(err)

        if f(mid) == 0 or err < tol:
            return {"root": mid, "iterations": i, "errors": errors, "method": "Bisection"}

        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

    return {"root": (a + b) / 2.0, "iterations": max_iter, "errors": errors, "method": "Bisection"}


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson Method
    ----------------------
    Finds root of f(x) = 0 given derivative df(x).

    Parameters:
        f        : callable, the function
        df       : callable, derivative of f
        x0       : float, initial guess
        tol      : float, tolerance for convergence
        max_iter : int, maximum iterations

    Returns:
        dict with root, iterations, error history
    """
    x = x0
    errors = []

    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero. Newton-Raphson failed.")

        x_new = x - fx / dfx
        err = abs(x_new - x)
        errors.append(err)

        if err < tol:
            return {"root": x_new, "iterations": i, "errors": errors, "method": "Newton-Raphson"}

        x = x_new

    return {"root": x, "iterations": max_iter, "errors": errors, "method": "Newton-Raphson"}


def secant(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Secant Method
    -------------
    Finds root of f(x) = 0 using two initial guesses (no derivative needed).

    Parameters:
        f        : callable, the function
        x0, x1   : float, two initial guesses
        tol      : float, tolerance for convergence
        max_iter : int, maximum iterations

    Returns:
        dict with root, iterations, error history
    """
    errors = []

    for i in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)

        if f1 - f0 == 0:
            raise ZeroDivisionError("Division by zero in Secant method.")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        err = abs(x2 - x1)
        errors.append(err)

        if err < tol:
            return {"root": x2, "iterations": i, "errors": errors, "method": "Secant"}

        x0, x1 = x1, x2

    return {"root": x1, "iterations": max_iter, "errors": errors, "method": "Secant"}
