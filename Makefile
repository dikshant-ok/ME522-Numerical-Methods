# Makefile for ME-522 Numerical Methods Project
# Usage:
#   make run      — run the main demo
#   make test     — run all unit tests
#   make plot     — generate convergence plot
#   make clean    — remove generated files
#   make help     — show this message

PYTHON = python3

.PHONY: run test plot clean help

run:
	$(PYTHON) main.py

test:
	$(PYTHON) -m pytest test_root_finding.py -v

plot:
	$(PYTHON) plot_convergence.py

clean:
	rm -f convergence_plot.png
	rm -rf __pycache__ .pytest_cache
	find . -name "*.pyc" -delete

help:
	@echo ""
	@echo "  make run    - Run the demo (main.py)"
	@echo "  make test   - Run unit tests"
	@echo "  make plot   - Generate convergence plot"
	@echo "  make clean  - Remove generated files"
	@echo ""
