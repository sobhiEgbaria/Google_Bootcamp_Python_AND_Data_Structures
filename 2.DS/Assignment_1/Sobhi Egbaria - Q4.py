# # Question 4, clause a
# # def unique_character(str):
# #     """Finds the index of the first non-repeating character in the string,
# #     or returns (-1) if no such index exists."""
# #     my_dict = {}
# #     for i in range(len(str)):
# #         if str[i] not in my_dict:
# #             my_dict.get(str[i], 1)
# #         else:
# #             my_dict[str[i]] += 1
# #             if my_dict[str[i]] == 2:
# #                 return i


# # Question 4, clause b
# # def group_by_anagrams(lst):
# #     dict = {}
# #     result = []
# #     for i in lst:
# #         key = "".join(sorted(i))
# #         if key in dict.keys():
# #             dict[key].append(i)
# #             result.append(i)
# #         else:
# #             dict[key] = []

# #     return result


# # print(group_by_anagrams(["helo", "leho", "eohl", "ohle"]))


# # Question 4, clause c # o(n**2)
# def check_contiguous_sum(arr):
#     """Receives an array of integers and checks whether
#     there exists a contiguous subarray whose numbers sum to 0."""
#     for i in range(len(arr)):
#         total = 0
#         for j in range(i, len(arr)):
#             total += arr[j]
#             if total == 0:
#                 print('Sublist', (i, j))
