"""
main.py
-------
Demonstrates the root-finding library on example functions.
Run: python main.py
"""

import math
from root_finding import bisection, newton_raphson, secant


# ── Test Functions ──────────────────────────────────────────────────────────

def f1(x):
    """f(x) = x^3 - x - 2   (root near x = 1.5214)"""
    return x**3 - x - 2

def df1(x):
    """f'(x) = 3x^2 - 1"""
    return 3*x**2 - 1

def f2(x):
    """f(x) = cos(x) - x   (root near x = 0.7391)"""
    return math.cos(x) - x

def df2(x):
    """f'(x) = -sin(x) - 1"""
    return -math.sin(x) - 1

def f3(x):
    """f(x) = e^x - 3x   (root near x = 0.6190 and x = 1.5121)"""
    return math.exp(x) - 3*x

def df3(x):
    """f'(x) = e^x - 3"""
    return math.exp(x) - 3


# ── Print Helper ─────────────────────────────────────────────────────────────

def print_result(result):
    print(f"  Method     : {result['method']}")
    print(f"  Root       : {result['root']:.8f}")
    print(f"  Iterations : {result['iterations']}")
    print(f"  Final Error: {result['errors'][-1]:.2e}")
    print()


# ── Run Demos ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  Numerical Root-Finding Library — ME-522")
    print("=" * 50)

    print("\n[1] f(x) = x^3 - x - 2")
    print("-" * 30)
    print_result(bisection(f1, 1, 2))
    print_result(newton_raphson(f1, df1, x0=1.5))
    print_result(secant(f1, x0=1, x1=2))

    print("\n[2] f(x) = cos(x) - x")
    print("-" * 30)
    print_result(bisection(f2, 0, 1))
    print_result(newton_raphson(f2, df2, x0=0.5))
    print_result(secant(f2, x0=0, x1=1))

    print("\n[3] f(x) = e^x - 3x  (first root)")
    print("-" * 30)
    print_result(bisection(f3, 0, 1))
    print_result(newton_raphson(f3, df3, x0=0.5))
    print_result(secant(f3, x0=0, x1=1))
