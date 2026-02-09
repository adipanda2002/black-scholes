"""
Sanity checks and known test cases for Black-Scholes pricing.
Run with: python examples.py
"""

import math
from black_scholes import call_price, put_price


def put_call_parity_check(S: float, K: float, T: float, r: float, sigma: float) -> None:
    """
    Verify put-call parity: C - P = S - K*exp(-r*T).
    """
    C = call_price(S, K, T, r, sigma)
    P = put_price(S, K, T, r, sigma)
    lhs = C - P
    rhs = S - K * math.exp(-r * T)
    diff = abs(lhs - rhs)
    print(f"  Put-call parity: C - P = {lhs:.6f},  S - K*e^(-rT) = {rhs:.6f},  |diff| = {diff:.2e}")
    assert diff < 1e-9, f"Put-call parity violated: diff = {diff}"


def known_test_case() -> None:
    """
    One known case: S=100, K=100, T=1, r=5%, sigma=20%.
    Reference (e.g. Hull): call ≈ 10.45, put ≈ 5.57.
    """
    S, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.20
    C = call_price(S, K, T, r, sigma)
    P = put_price(S, K, T, r, sigma)
    print(f"  S={S}, K={K}, T={T}, r={r}, sigma={sigma}")
    print(f"  Call = {C:.4f}  (expected ~10.45)")
    print(f"  Put  = {P:.4f}  (expected ~5.57)")
    assert 10.0 < C < 11.0 and 5.0 < P < 6.0, "Prices outside expected range"


if __name__ == "__main__":
    print("Known test case (ATM, 1Y, 5% r, 20% vol):")
    known_test_case()
    print("\nPut-call parity check (same parameters):")
    put_call_parity_check(100.0, 100.0, 1.0, 0.05, 0.20)
    print("\nAll checks passed.")
