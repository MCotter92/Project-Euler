# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palendrome(x):
    """
    Checks if an object is a palemdrome.
    """
    list = []
    for i in str(x):
        list.append(i)
    if list == list[::-1]:
        return True


# checking all 3 didgit numbers if palindrome

pals = []
for i in range(999, 100, -1):
    for j in range(100, 999):
        k = i * j
        if is_palendrome(k) == True:
            pals.append(k)

print(max(pals))

# check to see if multiple of 3 digit numbers
