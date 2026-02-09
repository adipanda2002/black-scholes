# Black-Scholes Option Pricing

A small Python project to learn and implement the Black-Scholes formula for European options, with Greeks.

## Setup

```bash
cd black-scholes
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Project layout (as we build it)

- `black_scholes.py` — core formula (d1, d2, call/put price)
- `greeks.py` — Delta, Gamma, Theta, Vega, Rho
- `examples.py` — tests and sanity checks
- `main.py` — CLI

## Conventions

- **Time**: `T` is time to expiry in **years** (e.g. 30 days = 30/365).
- **Parameters**: spot `S`, strike `K`, rate `r`, volatility `sigma` (e.g. 0.20 = 20%).
