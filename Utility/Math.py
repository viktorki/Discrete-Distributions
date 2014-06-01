class Combinatorics:
    @classmethod
    def c(cls, n, k):
        result = 1
        for i in range(n - k + 1, n + 1):
            result *= i
        for i in range(2, k + 1):
            result /= i
        return result
