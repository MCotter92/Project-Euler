import math

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

factors = []
n = 20
# essentiall creating a factor tree of n
for i in range(2, math.ceil(math.sqrt(n))):
    while n % i == 0:
        factors.append(i)
        print("This is i:", i)
        n = n / i
        print("This is n:", n)

print(factors)
