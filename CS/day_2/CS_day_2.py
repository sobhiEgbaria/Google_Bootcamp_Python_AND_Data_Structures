# # Question 1
# def print_numbers_while():
#     i = 1
#     while i <= 10:
#         print(f"{i}")
#         i += 1


# print_numbers_while()
# pass


# # Question 2
# def print_numbers_for():
#     for i in range(1, 11):
#         print(f"{i}")


# print_numbers_for()
# pass


# #Question 3
# def count_vowels(s):
#     counter = 0
#     for char in s:
#         lowe_char = str.lower(char)
#         # lowe_char = char.lower() # Anther way to use lower
#         if (
#             lowe_char == "a"
#             or lowe_char == "e"
#             or lowe_char == "i"
#             or lowe_char == "o"
#             or lowe_char == "u"
#         ):
#             counter += 1
#     return counter


# print(count_vowels("Hello"))
# pass


# # Question 4
# def sum_numbers_while():
#     sum = 0
#     for i in range(1, 101):
#         sum += i
#     return sum


# print(sum_numbers_while())

# pass


# Question 5
# def print_multiplication_table(n):
#     for i in range(1, 11):
#         print(i * n)


# print_multiplication_table(4)
# pass


# # Question 6
# def calculate_average(lst):
#     sum = 0
#     avg = 0
#     for i in lst:
#         sum += i
#     avg = sum / len(lst)
#     return avg


# print(calculate_average([1, 2, 3, 4, 5]))
# pass


# # Question 7
# def print_reverse_string(s):
#     rev = s[::-1]
#     print(rev)


# print_reverse_string("Hello")
# pass


# # Question 8
# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         else:
#             return True


# print(is_prime(1))
# print(is_prime(7))
# pass


# # Question 9
# def filter_strings(lst):
#     five_char_list = []
#     for i in lst:
#         if len(i) > 5:
#             five_char_list.append(i)
#     return five_char_list


# print(
#     filter_strings(
#         ["Hello", "OpenAI", "AI", "ChatGPT"],
#     )
# )
# pass


# # Question 10
# def print_triangle(n):
#     for i in range(1, n + 1):
#         print(((n - i) * " "), end="")
#         for j in range(1, i + 1):
#             print("*", end="")
#         print("")


# print_triangle(3)
# pass


# # Question 11
# def print_opposite_triangle(n):
#     for i in range(n + 1, 1, -1):
#         print(((n + 1 - i) * " "), end="")
#         for j in range(i, 1, -1):
#             print("*", end="")
#         print("")


# print_opposite_triangle(3)
# pass


# # Question 12
# def print_combined_pattern(n):
#     print_triangle(n)
#     print_opposite_triangle(n)


# print_combined_pattern(3)
# pass
