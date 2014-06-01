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


class BernoulliDistribution(DiscreteDistribution):
    def __init__(self, p):
        DiscreteDistribution.__init__(self, lambda k: p ** k * (1 - p) ** (1 - k), p, p * (1 - p))
        self.p = p
        self.q = 1 - p


class GeometricDistribution(DiscreteDistribution):
    def __init__(self, p):
        DiscreteDistribution.__init__(self, lambda k: p * (1 - p) ** k, (1 - p) / p, (1 - p) / (p ** 2))
        self.p = p
        self.q = 1 - p
