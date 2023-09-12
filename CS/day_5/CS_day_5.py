# def create_student_dict():
#     """
#     1. Implement the method create_student_dict()
#     Description: This method creates a dictionary representing a student with their name, age, major and grades.
#     """
#     student = {}
#     student["name"] = "John"
#     student["age"] = 20
#     student["major"] = "Computer Science"
#     student["grades"] = [85, 90, 92, 88]
#     return student


# print(create_student_dict())
# pass


# def names_to_lengths(names):
#     """
#     2. Implement the method names_to_lengths(names)
#     Description: This method maps a list of names to a dictionary with names as keys and their lengths as values.
#     """
#     dic = {}

#     for i in names:
#         dic[i] = dic.get(i, len(i))
#     return dic


# print(names_to_lengths(["Alice", "Bob", "Charlie"]))

# pass


# def count_elements(elements):
#     """
#     3. Implement the method count_elements(elements)
#     Description: This method counts the occurrence of each element in a list and stores the result in a dictionary.
#     """
#     dic_frequency = {}

#     for i in elements:
#         counter = elements.count(i)
#         dic_frequency[i] = dic_frequency.get(i, counter)

#     return dic_frequency


# print(
#     count_elements(
#         [
#             "apple",
#             "banana",
#             "apple",
#             "cherry",
#             "banana",
#             "banana",
#         ]
#     )
# )
# pass


# def create_phonebook(names, numbers):
#     """
#     4. Implement the method create_phonebook(names, numbers)
#     Description: This method creates a phone book using a dictionary with names as keys and phone numbers as values.
#     """
#     phone_book = {}
#     for i in range(len(names)):
#         phone_book[names[i]] = phone_book.get(names[i], numbers[i])
#     return phone_book


# print(create_phonebook(["Alice", "Bob"], ["123", "456"]))
# pass


# def calculate_averages(students):
#     dic_with_ag = {}
#     """
#     5. Implement the method calculate_averages(students)
#     Description: This method calculates the average grade for each student in a list and stores the result in a new dictionary.
#     """
#     for i in range(len(students)):
#         avg = sum(students[i]["grades"]) / len(students[i]["grades"])
#         dic_with_ag[students[i]["name"]] = dic_with_ag.get(students[i]["name"], avg)
#     return dic_with_ag


# print(
#     calculate_averages(
#         [
#             {"name": "Alice", "grades": [85, 90, 92, 88]},
#             {"name": "Bob", "grades": [80, 85, 89, 90]},
#         ]
#     )
# )
# pass


# def merge_dicts(dict1, dict2):
#     """
#     6. Implement the method merge_dicts(dict1, dict2)
#     Description: This method merges two dictionaries, and if there are duplicate keys, it adds their values.
#     """

#     for i in dict2:
#         if i in dict1:
#             dict1[i] = dict1[i] + dict2[i]
#         dict1[i] = dict1.get(i, (dict2[i]))

#     return dict1


# print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))
# pass


# def words_to_lengths(words):
#     dic = {}
#     """
#     7. Implement the method words_to_lengths(words)
#     Description: This method takes a list of words and maps them to a dictionary with the words as keys and their lengths as values, ignoring duplicates.
#     """
#     for i in words:
#         dic[i] = dic.get(i, (len(i)))
#     return dic


# print(words_to_lengths(["apple", "banana", "cherry"]))
# pass


# def most_frequent(elements):
#     counter = 0
#     most_frequent_e = ""
#     """
#     8. Implement the method most_frequent(elements)
#     Description: This method returns the most frequently occurring element in a list.
#     """
#     for i in elements:
#         if counter < elements.count(i):
#             most_frequent_e = i

#     return most_frequent_e


# print(most_frequent([1, 2, 2, 3, 3, 3]))
# pass


# def search_product(products, search_name):
#     """
#     9. Implement the method search_product(products, search_name)
#     Description: This method allows a user to search for a product by name and retrieve the corresponding price from a list of dictionaries representing products and their prices.
#     """
#     for i in range(len(products)):
#         if products[i]["name"] == search_name:
#             return products[i]["price"]


# print(
#     search_product(
#         [
#             {"name": "apple", "price": 1.0},
#             {"name": "banana", "price": 0.5},
#             {"name": "cherry", "price": 0.75},
#         ],
#         "banana",
#     )
# )
# pass


# def dict_to_tuples(dictionary):
#     lst = []
#     """
#     10. Implement the method dict_to_tuples(dictionary)
#     Description: This method converts a dictionary into a list of tuples, with each tuple representing a key-value pair.
#     """
#     for i in dictionary:
#         lst.append((i, dictionary[i]))
#     return lst


# print(dict_to_tuples({"a": 1, "b": 2, "c": 3}))
# pass
