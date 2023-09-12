# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact


# print(factorial(6))


# def chars_appear(chars_str):
#     dict_of_chars = {}
#     for i in chars_str:
#         if i in dict_of_chars:
#             dict_of_chars[i] += 1
#         else:
#             dict_of_chars[i] = 0
#             dict_of_chars[i] += 1
#     return dict_of_chars


# print(chars_appear("abcedrfgtdksmrtekandle"))


# ## solving with get
# def chars_appear(chars_str):
#     dict_of_chars = {}
#     for i in chars_str:
#         dict_of_chars[i] = dict_of_chars.get(i, 0) + 1
#     ## go to  dict_of_chars[i]
#     # use ((get)) to check the value of dict_of_chars[i] if dic in the {} return i + 1
#     # if dict_of_chars[i] not in dic ==>  dict_of_chars[i] = 0 and + 1

#     dict_of_chars_keys = dict_of_chars.keys()
#     sorted_dict = sorted(dict_of_chars_keys, key=dict_of_chars.get)
#     # key=dict_of_chars.get مش واضح منيح العمل: ترتيب حسب القيمة

#     for i in sorted_dict:
#         print((f"{i}: {dict_of_chars[i]}"))
#     return dict_of_chars, sorted_dict


# print(chars_appear("abcedrfgtdksmrtekandle"))


# def foo(a):
#     if len(foo) == 2 or len(foo) == 1:
#         return foo[0] + foo[1]
#     else:
#         return foo()


# print(foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# def reverse_string(s):
#     if len(s) == 0:
#         return
#     else:
#         words = s.split(" ")
#         last_word = words[(len(words) - 1)]
#         del words[-1]
#         shorter_sentens = " ".join(words)

#     return print(last_word), reverse_string(shorter_sentens)


# reverse_string("hi my name is sobhi")


# from math import pi

# print(pi)

# import math

# print(math.pi)


# class person:
#     def __init__(self, name: str, Id: int) -> None:
#         self.name = name
#         self.Id = Id


# class student(person):
#     def __init__(self, name: str, Id: int) -> None:
#         super().__init__(name, Id)
###### ###### ###### ###### ###### ####### ###### ####### ###### ###### #######


# def selectionSort(array):
#     for step in range(len(array)):
#         min_idx = step

#         for i in range(step + 1, len(array)):
#             # to sort in descending order, change > to < in this line
#             # select the minimum element in each loop
#             if array[i] < array[min_idx]:
#                 min_idx = i

#         # put min at the correct position
#         (array[step], array[min_idx]) = (array[min_idx], array[step])
#     return array


# data = [-2, 45, 0, 11, -9]
# print(
#     selectionSort( data,))


## ###################################################################point class

# from math import sqrt


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def print_point(self):
#         print(f"({self.x},{self.y})")

#     def distance(self, other):
#         return sqrt((self.x - other.x) ** 2 + (self.y - other.y))

#     def __repr__(self):
#         return "thi is gogo lolo foo"


# p1 = Point(1, 2)
# p2 = Point(2, 2)

# print(p1.distance(p2))
# print(p1)
