# need to check if a+b+c = 1000 and if a,b,c make a pythagorean triplet.
# a pythoagorean triplet means that a<b<c and a^2+b^2=c^2

from itertools import product


def PythCheck(n):
    for a, b, c in product(range(n), repeat=3):
        if (
            a + b + c == 1000
            and a**2 + b**2 == c**2
            and (a != 0 and b != 0 and c != 0)
            and a < b < c
        ):
            return a * b * c


print(PythCheck(1000))
