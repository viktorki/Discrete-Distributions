import math
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
