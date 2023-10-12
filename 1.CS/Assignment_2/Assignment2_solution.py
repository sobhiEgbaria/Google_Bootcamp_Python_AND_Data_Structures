## sobhi Egbaria 204442396

"""
1) Nested list: A nested list is a list within another list. 
The nested list can also be a list of lists.
Implement the recursive function `flatten_list(nested_lst)` that 
takes a nested list and returns a new list with all values without any nesting. 
There is no restriction over the nesting depth The solution must be recursive.
"""
### first solution:

# new_list = []  # global list (for me )


# def flatten_list(nested_lst):
#     for i in nested_lst:
#         if type(i) != list:
#             new_list.append(i)
#         else:
#             flatten_list(i)  # function call her self to track all the [].
#     return new_list


# print(flatten_list([1, [2, 4], [[[[[3], 2]], 1, 2], 4]]))


# ### second solution:


# def flatten_list(lst):
#     if lst == []:
#         return lst
#     if type(lst[0]) == list:
#         return flatten_list(lst[0]) + flatten_list(lst[1:])
#     return lst[:1] + flatten_list(lst[1:])


# print(flatten_list([1, [2, 4], [[[[[3], 2]], 1, 2], 4]]))


"""
Given two strings word1 and word2, find the minimum number of operations required to
convert word1 to word2. You have the following three operations available:
● Insert a character
● Delete a character
● Replace a character
Write a Python function min_edit_distance(word1, word2) that takes two strings as input
and returns the minimum edit distance required to transform word1 into word2.
min_edit_distance should use a recursive helper function, and you must use memoization
to optimize your solution and avoid redundant calculations.
You can assume valid input.


# """

# the function doesn't work i tried to solve it but i didn't success


def min_edit_distance(word1, word2):
    if len(word1) == 0:
        return word1
    if len(word2) == 0:
        return word2
    if word1[-1] == word2[-1]:
        min_edit_distance(word1[-1], word2[-1])
    else:
        return 0 + min(
            min_edit_distance(word1, word2[:-1]),  # to insert
            min_edit_distance(word1[:-1], word2),  # to delete
            min_edit_distance(word1[:-1], word2[:-1]),  # to replace
        )


print(min_edit_distance("intention", "execution"))

"""
3) BankAccount Class:
Create a class called `BankAccount` with the following attributes and methods:
"""


class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    pass

    def deposit(self, amount: float):
        self.amount = amount
        self.balance += amount

    pass

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= amount

    def get_balance(self):
        return self.balance


pass
