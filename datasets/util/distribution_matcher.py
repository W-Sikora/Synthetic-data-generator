from fitter import Fitter, get_common_distributions, get_distributions
from numpy import array

common = [
    "cauchy",
    "chi2",
    "expon",
    "exponpow",
    "gamma",
    "lognorm",
    "norm",
    "powerlaw",
    "rayleigh",
    "uniform",
    "poisson"
]


def match_distribution(column: array):
    fitter = Fitter(column, distributions=get_common_distributions())
    fitter.fit()
    return fitter.get_best()
