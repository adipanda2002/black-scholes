"""
Black-Scholes Greeks (sensitivities) for European options.
All times in years; volatility sigma as decimal (e.g. 0.20 = 20%).
"""

import math
from scipy.stats import norm

from black_scholes import d1, d2


def delta_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Delta of a European call: dV/dS = N(d1).
    Approximate change in call price per unit increase in spot.
    """
    return norm.cdf(d1(S, K, T, r, sigma))


def delta_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Delta of a European put: dV/dS = N(d1) - 1.
    Approximate change in put price per unit increase in spot.
    """
    return norm.cdf(d1(S, K, T, r, sigma)) - 1.0


def gamma(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Gamma (same for call and put): d²V/dS² = n(d1) / (S * sigma * sqrt(T)).
    Rate of change of Delta with respect to spot; n = standard normal PDF.
    """
    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma must be positive")
    _d1 = d1(S, K, T, r, sigma)
    return norm.pdf(_d1) / (S * sigma * math.sqrt(T))


def theta_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Theta of a European call: dV/dt (time decay, t = current time).
    Per one year; negative for long option. Divide by 365 for per-day.
    """
    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma must be positive")
    _d1 = d1(S, K, T, r, sigma)
    _d2 = d2(S, K, T, r, sigma)
    term1 = -S * norm.pdf(_d1) * sigma / (2 * math.sqrt(T))
    term2 = -r * K * math.exp(-r * T) * norm.cdf(_d2)
    return term1 + term2


def theta_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Theta of a European put: dV/dt (time decay).
    Per one year; negative for long option. Divide by 365 for per-day.
    """
    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma must be positive")
    _d1 = d1(S, K, T, r, sigma)
    _d2 = d2(S, K, T, r, sigma)
    term1 = -S * norm.pdf(_d1) * sigma / (2 * math.sqrt(T))
    term2 = r * K * math.exp(-r * T) * norm.cdf(-_d2)
    return term1 + term2


def vega(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Vega (same for call and put): dV/d(sigma) = S * n(d1) * sqrt(T).
    Change in option value per unit increase in volatility (e.g. 0.01 = 1%).
    """
    if T <= 0:
        raise ValueError("T must be positive")
    _d1 = d1(S, K, T, r, sigma)
    return S * norm.pdf(_d1) * math.sqrt(T)


def rho_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Rho of a European call: dV/dr = K * T * exp(-r*T) * N(d2).
    Change in call value per unit increase in risk-free rate.
    """
    _d2 = d2(S, K, T, r, sigma)
    return K * T * math.exp(-r * T) * norm.cdf(_d2)


def rho_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Rho of a European put: dV/dr = -K * T * exp(-r*T) * N(-d2).
    Change in put value per unit increase in risk-free rate.
    """
    _d2 = d2(S, K, T, r, sigma)
    return -K * T * math.exp(-r * T) * norm.cdf(-_d2)
