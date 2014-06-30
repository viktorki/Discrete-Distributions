import math
import random
from Utility.Math import Combinatorics

class DiscreteDistribution:
    def __init__(self, probability_density_function, expectation = 0, variance = 0):
        self.probability_density_function = probability_density_function
        if type(probability_density_function) is dict:
            self.custom = True
            self.expectation = 0
            for value, probability in probability_density_function.items():
                self.expectation += value * probability
            self.variance = 0
            for value, probability in probability_density_function.items():
                self.variance += (value - self.expectation) ** 2 * probability
        else:
            self.custom = False
            self.expectation = expectation
            self.variance = variance


class BinomialDistribution(DiscreteDistribution):
    def __init__(self, n, p):
        DiscreteDistribution.__init__(self, lambda k: Combinatorics.c(n, k) * p ** k * (1 - p) ** (n - k), n * p, n * p * (1 - p))
        self.n = n
        self.p = p
        self.q = 1 - p
    
    name = "Биномно разпределение"
    parameter_count = 2


class BernoulliDistribution(DiscreteDistribution):
    def __init__(self, p):
        DiscreteDistribution.__init__(self, lambda k: p ** k * (1 - p) ** (1 - k), p, p * (1 - p))
        self.p = p
        self.q = 1 - p
    
    name = "Бернулиево разпределение"
    parameter_count = 1


class GeometricDistribution(DiscreteDistribution):
    def __init__(self, p):
        DiscreteDistribution.__init__(self, lambda k: p * (1 - p) ** k, (1 - p) / p, (1 - p) / (p ** 2))
        self.p = p
        self.q = 1 - p
    
    name = "Геометрично разпределение"
    parameter_count = 1


class NegativeBinomialDistribution(DiscreteDistribution):
    def __init__(self, r, p):
        DiscreteDistribution.__init__(self, lambda k: Combinatorics.c(k - 1, r - 1) * p ** r * (1 - p) ** (k - r), r / p, r * (1 - p) / (p ** 2))
        self.r = r
        self.p = p
        self.q = 1 - p
    
    name = "Отрицателно биномно разпределение"
    parameter_count = 2


class HypergeometricDistribution(DiscreteDistribution):
    def __init__(self, N, M, n):
        DiscreteDistribution.__init__(self, lambda k: Combinatorics.c(M, k) * Combinatorics.c(N - M, n - k) / Combinatorics.c(N, n), n * M / N, n * M * (N - M) * (N - n) / (N ** 2 * (N - 1)))
        self.N = N
        self.M = M
        self.n = n
    
    name = "Хипергеометрично разпределение"
    parameter_count = 3


class PoissonDistribution(DiscreteDistribution):
    def __init__(self, mu):
        DiscreteDistribution.__init__(self, lambda k: mu ** k * math.e ** (-mu) / math.factorial(k), mu, mu)
        self.mu = mu
        
    def timeUntilNextOccurrence(self):
        return -math.log(1 - random.random()) / self.mu
    
    name = "Поасоново разпределение"
    parameter_count = 1
