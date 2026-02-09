"""
Simple Black-Scholes plots for exploration.
Run with: python plots.py
Generates price and Greeks vs spot S (fixed K, T, r, sigma).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from black_scholes import call_price, put_price
from greeks import delta_call, delta_put, gamma, vega

# Default parameters (K, T, r, sigma fixed; S varies)
K, T, r, sigma = 100.0, 1.0, 0.05, 0.20
S_grid = np.linspace(60, 140, 200)


def plot_price_vs_spot() -> None:
    """Call and put price vs spot S."""
    calls = np.array([call_price(S, K, T, r, sigma) for S in S_grid])
    puts = np.array([put_price(S, K, T, r, sigma) for S in S_grid])
    plt.figure(figsize=(8, 5))
    plt.plot(S_grid, calls, label="Call")
    plt.plot(S_grid, puts, label="Put")
    plt.axvline(K, color="gray", linestyle="--", alpha=0.7, label=f"Strike K={K}")
    plt.xlabel("Spot S")
    plt.ylabel("Option price")
    plt.title(f"Black-Scholes price vs spot (K={K}, T={T}, r={r}, σ={sigma})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("price_vs_spot.png", dpi=120)
    plt.close()
    print("Saved price_vs_spot.png")


def plot_greeks_vs_spot() -> None:
    """Delta, Gamma, Vega vs spot S."""
    deltas_c = np.array([delta_call(S, K, T, r, sigma) for S in S_grid])
    deltas_p = np.array([delta_put(S, K, T, r, sigma) for S in S_grid])
    gammas = np.array([gamma(S, K, T, r, sigma) for S in S_grid])
    vegas = np.array([vega(S, K, T, r, sigma) for S in S_grid])

    fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
    axes[0].plot(S_grid, deltas_c, label="Call Delta")
    axes[0].plot(S_grid, deltas_p, label="Put Delta")
    axes[0].axvline(K, color="gray", linestyle="--", alpha=0.7)
    axes[0].set_ylabel("Delta")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(S_grid, gammas, color="green", label="Gamma")
    axes[1].axvline(K, color="gray", linestyle="--", alpha=0.7)
    axes[1].set_ylabel("Gamma")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(S_grid, vegas, color="purple", label="Vega")
    axes[2].axvline(K, color="gray", linestyle="--", alpha=0.7)
    axes[2].set_xlabel("Spot S")
    axes[2].set_ylabel("Vega")
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    fig.suptitle(f"Greeks vs spot (K={K}, T={T}, r={r}, σ={sigma})")
    plt.tight_layout()
    plt.savefig("greeks_vs_spot.png", dpi=120)
    plt.close()
    print("Saved greeks_vs_spot.png")


if __name__ == "__main__":
    plot_price_vs_spot()
    plot_greeks_vs_spot()
    print("Done.")
