"""
CLI: Black-Scholes price and Greeks.
Usage: python main.py --S 100 --K 100 --T 1 --r 0.05 --sigma 0.2 [--type call|put|both]
T is time to expiry in years (e.g. 30 days = 30/365).
"""

import argparse

from black_scholes import call_price, put_price
from greeks import (
    delta_call,
    delta_put,
    gamma,
    theta_call,
    theta_put,
    vega,
    rho_call,
    rho_put,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Black-Scholes European option price and Greeks.",
    )
    parser.add_argument("--S", type=float, required=True, help="Spot price")
    parser.add_argument("--K", type=float, required=True, help="Strike price")
    parser.add_argument("--T", type=float, required=True, help="Time to expiry (years)")
    parser.add_argument("--r", type=float, required=True, help="Risk-free rate (decimal, e.g. 0.05)")
    parser.add_argument("--sigma", type=float, required=True, help="Volatility (decimal, e.g. 0.20)")
    parser.add_argument(
        "--type",
        choices=["call", "put", "both"],
        default="both",
        help="Option type to report (default: both)",
    )
    args = parser.parse_args()

    S, K, T, r, sigma = args.S, args.K, args.T, args.r, args.sigma

    print(f"Inputs: S={S}, K={K}, T={T}, r={r}, sigma={sigma}")
    print()

    if args.type in ("call", "both"):
        C = call_price(S, K, T, r, sigma)
        print(f"Call price: {C:.4f}")
        print(f"  Delta: {delta_call(S, K, T, r, sigma):.4f}")
        print(f"  Theta: {theta_call(S, K, T, r, sigma):.4f} (per year)")
        print(f"  Rho:   {rho_call(S, K, T, r, sigma):.4f}")
    if args.type in ("put", "both"):
        P = put_price(S, K, T, r, sigma)
        print(f"Put price:  {P:.4f}")
        print(f"  Delta: {delta_put(S, K, T, r, sigma):.4f}")
        print(f"  Theta: {theta_put(S, K, T, r, sigma):.4f} (per year)")
        print(f"  Rho:   {rho_put(S, K, T, r, sigma):.4f}")
    if args.type in ("call", "put", "both"):
        print(f"Gamma (same for call/put): {gamma(S, K, T, r, sigma):.6f}")
        print(f"Vega (same for call/put):  {vega(S, K, T, r, sigma):.4f}")


if __name__ == "__main__":
    main()
