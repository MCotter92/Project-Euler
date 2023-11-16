# define Sum of Squares


def SumSquare(n):
    """
    Choose an n. This function will sum the squares of all the natureal numbers up to n.
    """

    list = []
    for i in range(1, n + 1, 1):
        list.append(i)

    list2 = []
    for j in list:
        j = j**2
        list2.append(j)

    return sum(list2)


def SquareSum(n):
    """
    Choose an n. This function will square the sum of all the natureal numbers up to n.
    """

    list = []
    for i in range(1, n + 1, 1):
        list.append(i)

    s = sum(list)

    s = s**2

    return s


print(SquareSum(100) - SumSquare(100))
