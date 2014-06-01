from DiscreteRandomVariables.DiscreteDistribution import *
import random
class DiscreteRandomVariable:
    def __init__(self, distribution):
        self.custom_distribution = distribution.custom
        self.probability_density_function = distribution.probability_density_function
        self.expectation = distribution.expectation
        self.variance = distribution.variance
        self.standard_deviation = self.variance ** 0.5
    
    def getPossibleValue(self):
        generated = random.random()
        probability_distribution = 0
        if self.custom_distribution:
            for value, probability in self.probability_density_function.items():
                probability_distribution += probability
                if probability_distribution >= generated:
                    return value
        else:
            current = 0
            while(True):
                probability_distribution += self.probability_density_function(current)
                if probability_distribution >= generated:
                    return current
                current += 1
