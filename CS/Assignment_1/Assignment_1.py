"""
1.1) Implement the function `string_length(lst)` that takes a list of strings as input
and returns the length of the longest string.
Examples:
Input: ["this Is long", "short", "List of strings"]
Output: 15
"""


# def string_length(lst):
#     str_length = 0
#     for i in range(len(lst)):
#         if len(lst[i]) > str_length:
#             str_length = len(lst[i])
#     return str_length


# print(string_length(["this Is long", "short", "List of strings"]))

# *_**_*_*_*_*_*_*_*_*__*__*_*_*_*_*_*_*_*_*_*_*_*_*_**_*__*_*_*_*_*_*_*_*_*_*_*_*_*__*__

"""
1.2) Implement the function `list_average(lst)` that takes a list of numbers and
returns their average, median and sum.
Input-Output Examples:
Input : [1, 5, 2, 8, 10, 19]
Output: 7.5, 6.5, 45
"""


# def list_average(lst):
#     sum = 0
#     avg = 0
#     median = 0

#     for i in range(len(lst)):
#         sum += lst[i]
#     avg = sum / len(lst)
#     if len(lst) % 2 != 0:
#         median = lst[len(lst) // 2]
#     else:
#         median = (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

#     return (avg, median, sum)


# print(list_average([1, 5, 2, 8, 10, 19]))
# *_**_*_*_*_*_*_*_*_*__*__*_*_*_*_*_*_*_*_*_*_*_*_*_**_*__*_*_*_*_*_*_*_*_*_*_*_*_*__*__

"""
1.3)Implement the function `count_occurrences(lst, element)` 
that counts the number of occurrences of an element in a list and returns that count.
Input-Output Examples:
Input: [1, 5, 2, 8, 10, 2, 4, 2], 2
Output:3
"""

## first function using list.count()

# def count_occurrences(lst, element):
#     occurrences = lst.count(element)
#     return occurrences


# print(count_occurrences([1, 5, 2, 8, 10, 2, 4, 2], 2))

## second function using for loop


# def count_occurrences(lst, element):
#     occurrences = 0
#     for i in lst:
#         if i == element:
#             occurrences += 1
#     return occurrences


# print(count_occurrences([1, 5, 2, 8, 10, 2, 4, 2], 2))

# *_**_*_*_*_*_*_*_*_*__*__*_*_*_*_*_*_*_*_*_*_*_*_*_**_*__*_*_*_*_*_*_*_*_*_*_*_*_*__*__

"""
2) Implement the function `string_to_tuple(string)` that takes a string and 
returns a tuple where each element of the tuple is a character from the string.
The solution should be without casting. 
Input-Output Examples:
Input :  "Hello World"
Output: ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
"""


# def string_to_tuple(string):
#     tup = ()
#     for i in string:
#         i = (i,)
#         tup += i

#     return tup


# print(string_to_tuple("Hello World"))

# *_**_*_*_*_*_*_*_*_*__*__*_*_*_*_*_*_*_*_*_*_*_*_*_**_*__*_*_*_*_*_*_*_*_*_*_*_*_*__*__

"""
3)Implement the function `copy_list(lst)` that takes a list and
returns a copy of that list, 
ensuring that changes to the copied list do not affect the original list.
Input-Output Examples:
Input : ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

"""

# def copy_list(lst):
#     copy_lst = []
#     for i in lst:
#         copy_lst.append(i)
#     return copy_lst


# print(copy_list(["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"]))

# *_**_*_*_*_*_*_*_*_*__*__*_*_*_*_*_*_*_*_*_*_*_*_*_**_*__*_*_*_*_*_*_*_*_*_*_*_*_*__*__

"""
4) An anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, using all the original letters exactly once. 
For example, the word binary-brainy and the word adobe-abode.
function `is_anagram(str1, str2)` that checks if two input strings are anagrams.
The function should return True if the input strings are anagrams, and False otherwise.
Input-Output Examples:
Input :  "dad", "bad"
Output: False

Input-Output Examples:
Input :  "listen", "silent"
Output: True
"""


# def is_anagram(str1, str2):
#     is_anagram = True
#     for i in str1:
#         if i not in str2:
#             return False
#     else:
#         is_anagram = True
#     for i in str2:
#         if i not in str1:
#             return False
#     else:
#         is_anagram = True
#     return is_anagram


# print(is_anagram("dad", "bad"))

# *_**_*_*_*_*_*_*_*_*__*__*_*_*_*_*_*_*_*_*_*_*_*_*_**_*__*_*_*_*_*_*_*_*_*_*_*_*_*__*__
"""
5)Implement the function `rotate_matrix(matrix)` that takes a 2D list (matrix) n*m and 
rotates it 90 degrees to the right -> m*n. 
Input-Output Examples:

Input: [[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 12]]

Output: [[9, 5, 1]
[10, 6, 2]
[11, 7, 3]
[12, 8, 4]]
"""


# def rotate_matrix(matrix):
#     rotate_matrix = []
#     while_condition = len(matrix)

#     while while_condition > 0:
#         j = 0
#         temp = []
#         for i in range(len(matrix)):
#             temp.append(matrix[i][j])
#             del matrix[i][j]

#         temp.reverse()
#         rotate_matrix.append(temp)
#         while_condition -= 1

#     return (rotate_matrix, matrix)


# print(rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# *_**_*_*_*_*_*_*_*_*__*__*_*_*_*_*_*_*_*_*_*_*_*_*_**_*__*_*_*_*_*_*_*_*_*_*_*_*_*__*__

"""
6)Implement the function `flatten_list_max_three(nested_lst)`
that takes a nested list and returns a new list with all values without any nesting. 
The nesting depth is restricted to max 3. Do not use casting to list. 
For example = [1,[2,4],[[1,2],4]]]
Input-Output Examples:
Input :  [1, [2, 4], [[1, 2], 4]]
Output: [1, 2, 4, 1, 2, 4]

"""


# def flatten_list_max_three(nested_lst):
#     new_list = []

#     for i in range(len(nested_lst)):
#         if type(nested_lst[i]) != list:
#             new_list.append(nested_lst[i])
#         else:
#             for j in range(len(nested_lst[i])):
#                 if type(nested_lst[i][j]) != list:
#                     new_list.append(nested_lst[i][j])
#                 else:
#                     for n in range(len(nested_lst[i][j])):
#                         if type(nested_lst[i][j][n]) != list:
#                             new_list.append(nested_lst[i][j][n])

#     return new_list


# print(flatten_list_max_three([1, [2, 4], [[1, 2], 4]]))

# *_**_*_*_*_*_*_*_*_*__*__*_*_*_*_*_*_*_*_*_*_*_*_*_**_*__*_*_*_*_*_*_*_*_*_*_*_*_*__*__

"""
7) Bonus: Implement the function `flatten_list(nested_lst)` that takes a nested list
and returns a new list with all values without any nesting. 
There is no restriction over the nesting depth .Do not use casting to list. 
Input-Output Examples:
Input :  [1, [2, 4], [[[[[3],2]], 1, 2], 4]]
Output: [1, 2, 4, 3, 2, 1, 2, 4]
"""

new_list = []  # global list (for me )


def flatten_list(nested_lst):
    for i in nested_lst:
        if type(i) != list:
            new_list.append(i)
        else:
            flatten_list(i)  # function call her self to track all the [].
    return new_list


print(flatten_list([1, [2, 4], [[[[[3], 2]], 1, 2], 4]]))

# note: you can use the function in 7 to solve also 6 ... 6 is a simple case of 7
