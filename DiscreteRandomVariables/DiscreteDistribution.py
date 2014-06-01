from Utility.Math import Combinatorics
class DiscreteDistribution:
    def __init__(self, distribution, expectation, variance):
        self.distribution = distribution
        self.expectation = expectation
        self.variance = variance

class BinomialDistribution(DiscreteDistribution):
    def __init__(self, n, p):
        DiscreteDistribution.__init__(self, lambda k: Combinatorics.c(n, k) * p ** k * (1 - p) ** (n - k), n * p, n * p * (1 - p))
        self.n = n
        self.p = p
        self.q = 1 - p
