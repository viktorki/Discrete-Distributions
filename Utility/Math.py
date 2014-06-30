import math
import random

class Combinatorics:
    @classmethod
    def c(cls, n, k):
        n = int(n)
        k = int(k)
        result = 1
        for i in range(n - k + 1, n + 1):
            result *= i
        result /= math.factorial(k)
        return result

class Set:
    @classmethod
    def randomSubset(cls, n, m):
        result = [0 for _ in range(n)]
        generated = 0
        while generated < m:
            position = int(n * random.random())
            if result[position] == 0:
                result[position] = 1
                generated += 1
        return result
