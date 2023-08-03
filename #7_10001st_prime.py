# I don't want to check all 10001 numbers so there has to be a number theory approach to this.

# Need to check if a number is prime.
from math import isqrt


def PrimeCheck(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0 or n % 7 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


# Found this algorithm on the web after multiple failed attempts to make my method of simply checking all numbers between 2 and sqrt(n) more light weight failed. Seems to work pretty well and I really find the mathematics of it interesting. 6 really is a cool number.

# Next I need to find a way to create a list with a cardinality determined by the user, that is made up of primes.

cardinality = 10001
primes = []
i = 1

while len(primes) < cardinality:
    if PrimeCheck(i) == True:
        primes.append(i)
    i = i + 1

print(primes[-1])
