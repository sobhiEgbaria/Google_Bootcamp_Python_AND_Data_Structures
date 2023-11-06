"""
I am shouting your words:
GOOD MORNING WORLD

Your words as a title:
Good Morning World

Your words as an inverse title:
gOOD mORNING wORLD

"""


# sentence = input("Please enter a sentence:\n >")

# print("I am shouting your words:")
# all_letter_up = ""
# for i in sentence:
#     all_letter_up += i.capitalize()
# print(all_letter_up)

# print("Your words as a title:")
# print(f"{sentence.title()}")

# print("Your words as an inverse title:")

# inverse_title = ""
# sentence_list = sentence.split()
# for i in sentence_list:
#     inverse_title += i[0:1] + i[1:].upper() + " "

# print(inverse_title)

## ===============================================================================
"""
prints Yummy! 
unless the entered word was all uppercase, prints OK BUT WHY ARE YOU SHOUTING? instead

"""
# word = input("Enter something you like to eat:\n ")

# if word.isupper():
#     print("OK BUT WHY ARE YOU SHOUTING?")
# else:
#     print("ymmmmi!!!")


## ===============================================================================
"""
example:
What is the product name? coffee
What is the price in NIS? 12.5
If the price includes VAT enter "y" (or otherwise anything else): n

>>>The price of coffee is 12.50 NIS + 2.12 VAT = 14.62 TOTAL.

Another example:
What is the product name? coffee
What is the price in NIS? 12.5
If the price includes VAT enter "y" (or otherwise anything else): y

>>>The price of coffee is 10.68 NIS + 1.82 VAT = 12.50 TOTAL.

"""
# product = input("What is the product name?\n >")
# price = float(input("What is the price in NIS ?\n >"))
# vat = input("If the price includes VAT enter y (or otherwise anything else): n\n >")
# tax = 0.17
# total = price + price * tax

# if vat == "y":
#     price = price * (100 / 117)
#     total = price
# print(
#     f"The price of {product} is {round(price,2)} NIS + {round(price*tax,2)} VAT = {round(total,2)} TOTAL."
# )

## ===============================================================================
# total = 0
# while True:
#     new_num = input("pleas enter a number:\n >")
#     if new_num == "":
#         break
#     total += int(new_num)

# print(total)
## ===============================================================================

"""
Create a multiplayer game!!

Player 2 looks to the other direction, while player 1 enters a secret number between 1 and 100. (use input() to get a number from the user)

The screen is cleared. (Print a lot of blank lines with "\n" * 100)

Player 2 returns and tries to guess the number. The computer might say Correct! You win! and the game is done.

Otherwise print Your guess is too high! or Your guess is too low! and ask again.
"""

# (secret_number) = int(input("enters a secret number between 1 and 100:\n >"))
# print("\n" * 100)

# while True:
#     guess = int(input("try to guess the number :\n >"))

#     if guess == secret_number:
#         print("Correct! You win!")
#         break
#     elif guess > secret_number:
#         print(f"Your guess is too high!")

#     else:
#         print(f"Your guess is too low!")

## ===============================================================================
"""
 Guessing game: Play against your PC!
"""
import random

(secret_number) = int(input("enters a secret number between 1 and 100:\n >"))
print("\n" * 100)
min_limit = 1
max_limit = 101

while True:
    guess = random.randrange(min_limit, max_limit)

    isRight = input(f"is the number (( {guess} )) ?\n >")

    if isRight == "y":
        print("Correct! You win!")
        break
    else:
        temp = input("Is my guess higher than the secret number?\n >")

        if temp == "y":
            print(f"Your guess is too high!")
            max_limit = guess

        else:
            print(f"Your guess is too low!")
            min_limit = guess + 1
## ===============================================================================
