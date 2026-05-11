# Numerical Methods Library — ME-522

A Python library implementing three classical root-finding methods:
- **Bisection**
- **Newton-Raphson**
- **Secant**

Built for the course **ME-522: High-Performance Scientific Computing**, IIT Mandi.

---

## Project Structure

```
numerical_methods/
├── root_finding.py        # Core library (all three methods)
├── main.py                # Demo: runs all methods on test functions
├── test_root_finding.py   # Unit tests (pytest)
├── plot_convergence.py    # Convergence plot generator
├── Makefile               # Shortcuts for common commands
└── README.md              # This file
```

---

## Setup & Usage

### 1. Install dependencies
```bash
pip install pytest matplotlib
```

### 2. Run the demo
```bash
make run
# or: python3 main.py
```

### 3. Run tests
```bash
make test
# or: python3 -m pytest test_root_finding.py -v
```

### 4. Generate convergence plot
```bash
make plot
# Saves: convergence_plot.png
```

---

## Git Setup (Version Control)

### Initialize and make first commit
```bash
git init
git add .
git commit -m "Initial commit: add root-finding library with bisection, Newton-Raphson, secant"
```

### Recommended branching workflow
```bash
# Create a feature branch for a new method
git checkout -b feature/add-brent-method

# After changes, commit and merge back
git add .
git commit -m "Add Brent's method for robust root finding"
git checkout main
git merge feature/add-brent-method
```

### Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/numerical-methods-me522.git
git push -u origin main
```

### Useful Git commands
```bash
git log --oneline        # View commit history
git diff                 # See uncommitted changes
git status               # Check working tree status
```

---

## Methods Summary

| Method | Derivative Needed? | Convergence Rate | Pros |
|---|---|---|---|
| Bisection | No | Linear | Always converges if bracket valid |
| Newton-Raphson | Yes | Quadratic | Very fast near root |
| Secant | No | Superlinear | Fast, no derivative required |

---

## Example Output

```
==================================================
  Numerical Root-Finding Library — ME-522
==================================================

[1] f(x) = x^3 - x - 2
  Method     : Bisection
  Root       : 1.52137970
  Iterations : 20
  Final Error: 9.54e-07

  Method     : Newton-Raphson
  Root       : 1.52137971
  Iterations : 5
  Final Error: 2.11e-12
  ...
```
