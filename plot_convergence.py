"""
plot_convergence.py
--------------------
Plots convergence (error vs iteration) for all three methods.
Run: python plot_convergence.py
Saves: convergence_plot.png
"""

import math
import matplotlib.pyplot as plt
from root_finding import bisection, newton_raphson, secant

# f(x) = x^3 - x - 2
f  = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1

r1 = bisection(f, 1, 2)
r2 = newton_raphson(f, df, x0=1.5)
r3 = secant(f, x0=1, x1=2)

fig, ax = plt.subplots(figsize=(8, 5))

ax.semilogy(r1["errors"], "o-", label="Bisection", color="#e63946", linewidth=2)
ax.semilogy(r2["errors"], "s-", label="Newton-Raphson", color="#2a9d8f", linewidth=2)
ax.semilogy(r3["errors"], "^-", label="Secant", color="#e9c46a", linewidth=2)

ax.set_xlabel("Iteration", fontsize=13)
ax.set_ylabel("Error (log scale)", fontsize=13)
ax.set_title("Convergence Comparison — f(x) = x³ − x − 2", fontsize=14)
ax.legend(fontsize=12)
ax.grid(True, which="both", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("convergence_plot.png", dpi=150)
print("Saved: convergence_plot.png")
plt.show()
