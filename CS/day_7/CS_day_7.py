def factorial(n):
    """
    Calculates the factorial of 'n' using recursion.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

pass

#################################################################################


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
pass

#################################################################################


def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


print(sum_list([1, 2, 3, 4, 5]))
pass

#################################################################################


def max_element(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        m = max_element(lst[1:])
        return m if m > lst[0] else lst[0]


print(max_element([1, 2, 3, 4, 9, 5, 8]))
pass

#################################################################################


def power(base, exponent):
    """
    Calculates the power of 'base' raised to 'exponent' using recursion.
    """
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


pass


#################################################################################


def reverse_string(s):
    """
    Reverses the string 's' using recursion.
    """
    if len(s) == 0:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]


print(reverse_string("ldfdsoo"))
pass


#################################################################################


def is_palindrome(s):
    """
    Checks if the string 's' is a palindrome using recursion.
    """
    pass


#################################################################################
def gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of 'a' and 'b' using recursion.
    """
    pass


#################################################################################
def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solves the Tower of Hanoi problem for 'n' disks using recursion.
    """
    pass


#################################################################################
def permutations(s):
    """
    Generates all permutations of the string 's' using recursion.
    """
    pass


#################################################################################
