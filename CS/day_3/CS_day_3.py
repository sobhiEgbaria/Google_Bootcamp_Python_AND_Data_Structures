# # Task 1
# def print_second_element_tuple():
#     fruits_tuple = ("apple", "banana", "cherry")
#     print(fruits_tuple[1])


# print_second_element_tuple()
# pass


# # Task 2
# def modify_tuple_copy():
#     fruits_tuple = ("apple", "banana", "cherry")
#     second_tuple = []
#     second_tuple.extend(fruits_tuple)
#     second_tuple.append("orange")
#     second_tuple = tuple(second_tuple)

#     print(f"{fruits_tuple}\n{second_tuple}")


# modify_tuple_copy()
# pass


# # Task 3
# def print_names_with_index(name):
#     lst = name
#     for i, e in enumerate(lst):
#         print(f"Index: {i}, Name: {e}")


# print_names_with_index(["Alice", "Bob", "Charlie"])
# pass


# # Task 4
# def mutable_immutable_demo():
#     tup = (1, 2, 3)
#     print(tup)

#     try:
#         tup[0] = 5

#     except TypeError:
#         print("Cannot modify a tuple")
#     lst = [1, 2, 3]
#     print(lst)
#     lst[0] = 5
#     print(lst)


# mutable_immutable_demo()
# pass


# # Task 5
# def demonstrate_aliasing():
#     a = [1, 2, 3]
#     b = a
#     a[0] = 5
#     print(f"{a}\n{b}")


# demonstrate_aliasing()
# pass


# # Task 6
# def print_string_slicing(s):
#     print(s[:3])
#     print(s[len(s) - 3 :])


# print_string_slicing("HelloWorld")
# pass


# # Task 7
# def sum_and_product_slicing(numbers):
#     even = sum(numbers[::2])
#     odd = numbers[1::2]
#     mult_odd = 1

#     for i in odd:
#         mult_odd *= i

#     print(f"{even}\n{mult_odd}")


# sum_and_product_slicing([1, 2, 3, 4, 5])
# pass


# # Task 8
# import copy

# def deep_copy_modify_nested_list():
#     lst = [[1, 2, 3], [4, 5, 6]]
#     copy_lst = copy.deepcopy(lst)
#     lst[0][0] = 100
#     print(f"{copy_lst}\n{lst}")


# deep_copy_modify_nested_list()
# pass


# # Task 9
# def month_slicing():
#     months = (
#         "January",
#         "February",
#         "March",
#         "April",
#         "May",
#         "June",
#         "July",
#         "August",
#         "September",
#         "October",
#         "November",
#         "December",
#     )

#     first_four = months[:4]
#     middle_four = months[4:8]

#     last_four = months[8:]

#     print(f"{first_four}\n{middle_four}\n{last_four}")


# month_slicing()
# pass


# # Task 10
# def print_every_second_reverse(numbers):
#     revers_num = numbers[-1::-2]

#     print(revers_num)


# print_every_second_reverse([1, 2, 3, 4, 5, 6, 7])

# pass
