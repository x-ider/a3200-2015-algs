import math


def sieve(n):
    a = [simple(x) for x in range(2, n + 1)]
    a.insert(0, False)
    return a


def simple(n):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True


n = input("Enter range: ")
print(sieve(int(n)))