# Black-Scholes Option Pricing

A small Python project to learn and implement the Black-Scholes formula for European options, with Greeks.

## Setup

```bash
cd black-scholes
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
# Sanity checks and put-call parity
python examples.py

# Price and Greeks from the command line
python main.py --S 100 --K 100 --T 1 --r 0.05 --sigma 0.2

# Plots: price and Greeks vs spot (writes price_vs_spot.png, greeks_vs_spot.png)
python plots.py
```

## Project layout

- `black_scholes.py` — core formula (d1, d2, call/put price)
- `greeks.py` — Delta, Gamma, Theta, Vega, Rho
- `examples.py` — tests and sanity checks
- `main.py` — CLI
- `plots.py` — optional plots (price and Greeks vs spot)

## Conventions

- **Time**: `T` is time to expiry in **years** (e.g. 30 days = 30/365).
- **Parameters**: spot `S`, strike `K`, rate `r`, volatility `sigma` (e.g. 0.20 = 20%).
