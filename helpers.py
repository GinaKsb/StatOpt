import numpy as np
import scipy.special

def pasc_coefficients(n: int): 
    """Returns the Pascals triangle coefficients for order n"""
    ls = [scipy.special.binom(n, k) for k in range(n+1)]
    return ls

def spacings(n: int):
    """Returns a list of numbers in the range of [0,1] spaced
    corresponding to the binomial distribution of order n"""
    ls = [0]
    coeff = pasc_coefficients(n)
    for i in range(1,n+2):
        ls.append(sum(coeff[0:i])*2**(-n))
    return ls





