# Find the sum of all primes below 2 million.

from p007 import PrimeCheck

sum = 0
for i in range(2000000):
    if PrimeCheck(i) == True:
        sum += i

print(sum)
