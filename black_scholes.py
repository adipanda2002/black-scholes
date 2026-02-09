"""
Black-Scholes formula for European options.

All times are in years. Volatility sigma is decimal (e.g. 0.20 = 20%).
"""

import math
from scipy.stats import norm


def d1(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Black-Scholes d1 parameter.

    d1 = (ln(S/K) + (r + sigma^2/2)*T) / (sigma * sqrt(T))

    Used in the call price (N(d1)) and in Delta. With risk-neutral drift
    r - sigma^2/2, d1 is the standardized log-moneyness plus one half
    of the volatility-scaled time.
    """
    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma must be positive")
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))


def d2(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Black-Scholes d2 parameter.

    d2 = d1 - sigma * sqrt(T)

    Equals the standardized log-moneyness under the risk-neutral measure.
    N(d2) is the risk-neutral probability that the call finishes in the money.
    """
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)


def call_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Black-Scholes European call option price.

    C = S * N(d1) - K * exp(-r*T) * N(d2)
    """
    _d1 = d1(S, K, T, r, sigma)
    _d2 = d2(S, K, T, r, sigma)
    return S * norm.cdf(_d1) - K * math.exp(-r * T) * norm.cdf(_d2)


def put_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Black-Scholes European put option price.

    P = K * exp(-r*T) * N(-d2) - S * N(-d1)
    """
    _d1 = d1(S, K, T, r, sigma)
    _d2 = d2(S, K, T, r, sigma)
    return K * math.exp(-r * T) * norm.cdf(-_d2) - S * norm.cdf(-_d1)
