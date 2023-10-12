# def first_program() -> None:
#     print("|------------------------------|")
#     print("|                              |")
#     print("| My first Python application! |")
#     print("|                              |")
#     print("|------------------------------|")


# first_program()

# pass


# def variables_separate_lines() -> None:
#     v1 = 1
#     v2 = 2
#     v3 = 3.14
#     v4 = False
#     print(v1)
#     print(v2)
#     print(v3)
#     print(v4)


# variables_separate_lines()
# pass


# def variables_single_line() -> None:
#     # v1 = 1
#     # v2 = 2
#     # v3 = 3.14
#     # v4 = False
#     print("1, 2, 3.14, False")


# variables_single_line()
# pass


# def intro() -> None:
#     name = "Alice"
#     birth_year = 1990
#     height = 1.7
#     print(
#         f"Hi, my name is {name}\nI was born in {birth_year}\nI am {height} meters tall"
#     )


# intro()

# pass


# def print_digits() -> None:
#     number = int(input("enter a number:\n"))  # 45
#     Units = number % 10
#     Tens = number // 10
#     print(f"Units: {Units}\nTens: {Tens}")


# print_digits()
# pass


# def average() -> None:
#     first_num = int(input("enter the first number:\n"))
#     second_num = int(input("enter the second number:\n"))
#     third_num = int(input("enter the third number:\n"))

#     sum = first_num + second_num + third_num
#     avg = sum / 3
#     print("The average of the numbers is", avg)


# average()
# pass


# def sum_digits() -> None:
#     num = int(input("enter the  4-dig number:\n")) #1234
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num = num // 10
#     print("Sum:", sum)


# sum_digits()
# pass


# def sec_to_time() -> None:
#     total_seconds = int(input("enter the seconds:\n"))
#     seconds = total_seconds % 60
#     min = ((total_seconds - seconds) // 60) % 60
#     hour = min % 60
#     print(hour, ":", min, ":", seconds)


# sec_to_time()
# pass


# def concat_str_and_int() -> None:
#     number = str(input("enter a number :\n"))
#     print("The number is", number)


# concat_str_and_int()
# pass
