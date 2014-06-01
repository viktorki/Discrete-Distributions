class DiscreteRandomVariable(object):
    def __init__(self, distribution):
        self.distribution = distribution
        self.expectation = 0
        for value, probability in distribution.items():
            self.expectation += value * probability
        self.variance = 0
        for value, probability in distribution.items():
            self.variance += (value - self.expectation) ** 2 * probability
        self.standard_deviation = self.variance ** 0.5

    def getExpectation(self):
        return self.expectation

    def getVariance(self):
        return self.variance

    def getStandardDeviation(self):
        return self.standard_deviation
    