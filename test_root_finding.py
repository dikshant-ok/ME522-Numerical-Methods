"""
test_root_finding.py
---------------------
Unit tests for the root-finding library.
Run: python -m pytest test_root_finding.py -v
"""

import math
import pytest
from root_finding import bisection, newton_raphson, secant

TOL = 1e-6

# ── Shared test functions ─────────────────────────────────────────────────────

f  = lambda x: x**3 - x - 2       # root ~ 1.52138
df = lambda x: 3*x**2 - 1

fc  = lambda x: math.cos(x) - x   # root ~ 0.73909
dfc = lambda x: -math.sin(x) - 1


# ── Bisection Tests ───────────────────────────────────────────────────────────

class TestBisection:
    def test_cubic(self):
        res = bisection(f, 1, 2)
        assert abs(res["root"] - 1.52138) < 1e-4

    def test_cosine(self):
        res = bisection(fc, 0, 1)
        assert abs(res["root"] - 0.73909) < 1e-4

    def test_opposite_signs_required(self):
        with pytest.raises(ValueError):
            bisection(f, 2, 4)   # f(2)=4 and f(4)=58, both positive

    def test_converges(self):
        res = bisection(f, 1, 2, tol=TOL)
        assert res["errors"][-1] < TOL


# ── Newton-Raphson Tests ──────────────────────────────────────────────────────

class TestNewtonRaphson:
    def test_cubic(self):
        res = newton_raphson(f, df, x0=1.5)
        assert abs(res["root"] - 1.52138) < 1e-5

    def test_cosine(self):
        res = newton_raphson(fc, dfc, x0=0.5)
        assert abs(res["root"] - 0.73909) < 1e-5

    def test_fast_convergence(self):
        res = newton_raphson(f, df, x0=1.5, tol=TOL)
        # Newton-Raphson should converge in very few iterations
        assert res["iterations"] < 15

    def test_zero_derivative_raises(self):
        # f(x) = x^2, df(x) = 2x — starting at 0 causes zero derivative
        with pytest.raises(ZeroDivisionError):
            newton_raphson(lambda x: x**2, lambda x: 2*x, x0=0)


# ── Secant Tests ──────────────────────────────────────────────────────────────

class TestSecant:
    def test_cubic(self):
        res = secant(f, x0=1, x1=2)
        assert abs(res["root"] - 1.52138) < 1e-4

    def test_cosine(self):
        res = secant(fc, x0=0, x1=1)
        assert abs(res["root"] - 0.73909) < 1e-4

    def test_converges(self):
        res = secant(f, x0=1, x1=2, tol=TOL)
        assert res["errors"][-1] < TOL

    def test_no_derivative_needed(self):
        # Secant only needs f, not df — should work fine
        res = secant(lambda x: x**2 - 4, x0=1, x1=3)
        assert abs(res["root"] - 2.0) < 1e-5
