import numpy as np
import math

intervals = 22

mu = 11
sigma = 5


# distribution function
def normal_dist(x, mu, sigma):
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


# TODO: FINISH IT!!

