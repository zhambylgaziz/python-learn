# Python lessons

# using Learn Python - Full Course for Beginners from freeCodeCamp.org
# https://youtu.be/rfscVS0vtbw

# --------------------------------------------------------------------
# 1 - String & Integer

# char_name = "Zhambyl"
# char_age = 19
# print("Hello, my name is "+char_name+", and I'm", char_age, "y.o")

# --------------------------------------------------------------------
# 2 - List

# can store any of data types
# array
# friends = ["Ammyy", "Jammy", "Gabby"]
#            0(-3)    1(-2)    2(-1)
# print(friends[-3])
# friends[1] = "Jimmy"
# print(friends[1:])

# --------------------------------------------------------------------
# 3 - List functions

# numbers = [4, 7, 14, 21 ,42]
# friends = ["Ammyy", "Jammy", "Gabby", "Jammy", "Kobby", "Tobby"]
# friends.extend(numbers) #add 2 lists together
# friends.append("Funny") #add 1 item to the end
# friends.insert(1, "Zeddy") #add item to chosen position
# friends.remove(14) #remove 1 item
# friends.clear(); #empty list
# friends.pop() #removes last item
# print(friends.index("Gabby")) #return item's index
# print(friends.count("Jammy")) #counts item
# friends.sort()  #sort by alphabetic order
# friends2 = friends.copy().reverse() #copies to friends2 and reverse it
# print(friends)

# --------------------------------------------------------------------
# 4 - Tumples

# data structure, similar to list.
# immutable - cannot be changed, modified, cannot add new elements, etc (final)
# coordinate = (4, 5)
# coordinates = [(1, 5), (3, 6), (8, 4)]
# print(coordinates[0])

# --------------------------------------------------------------------
# 5 - Functions

# collection of code which performs a specific task
# helps to organize code
# all lower case, use underscore

# def greeting():
#    print("Hello World!")
# greeting()

# parameter - piece of information that we give to function

# def greet_user(user):
#     print("Hello", user)

# greet_user("John")
# greet_user("Marry")

# --------------------------------------------------------------------
# 6 - Return Statement

# returning some info back, key word = 'return'

# def cube(num):
#     return num*num*num
# res = cube(6)
# print(res)

# --------------------------------------------------------------------
# 6 - If Statements

# is_male = True
# is_tall = False

# if is_male or is_tall:
#    print("male or short")

# if is_male and is_tall:
#    print("male and tall")
# elif is_male and not(is_tall):
#     print("male and short")
# elif not(is_male) and is_tall:
#     print("female and tall")
# else:
#     print("female and short")

# --------------------------------------------------------------------
# 7 - If Statements & Comparisions

# comparing numbers, strings, etc
# def max(num1, num2, num3):
#    if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num1 <= num2 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max(3, 4, 5))

# --------------------------------------------------------------------
# 8 - Calculator


# def calc(num1, op, num2):
#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#      elif op == "/":
#          print(num1 / num2)
#     else:
#         print("Invalid operator")

# num1 = float(input("Enter first number: " ))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
# calc(num1, op, num2)

# --------------------------------------------------------------------
# 9 - Dictionairies

# It is special structures, which allows to store information in kay-value pairs.

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
#     1: "January"
# }

# print(monthConversions["Feb"])
# print(monthConversions.get("Dec"))
# print(monthConversions.get("Luv", "Not a valid key"))
# if it is not on the dictionnaire, we can use default value
# print(monthConversions[1])

# --------------------------------------------------------------------
# 10 - While loop

# It is a structure in python, which allows to look through and  to execute block of code multiple times

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("loop end")

# --------------------------------------------------------------------
# 11 - Guessing game
# using if & else statement, loop, variables
# game until user will guess the secret word (secret_word = "elephant)
# user have limit to input (guess_limit = 3)
# secret_word = "elephant"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of Guesses, You lose")
# else:
#     print("You win!")

# --------------------------------------------------------------------
# 13 - For Loop

# Allows to loop over different collections (arrays, letters in array, etc.)

# for every letter in this string do smth
# for letter in "Some string":
#     print(letter)
# for each friend in friends print it
# friends = ["Jim", "Karen", "Kevin"]
# for friend in friends:
#     print(friend)
# print every number between 3 and 10, 10 doesn't included
# for index in range(3, 10):
#     print(index)

# --------------------------------------------------------------------
# 13 - Exponent Function
# take power of number

# 2^3 = 8
# print(2**3)

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result *= base_num
#     return result

# print(raise_to_power(2, 5))

# --------------------------------------------------------------------
# 14 - 2D Lists and Nested Loops

# number_grid = [
#     [1, 2, 3],  # row 0
#     [4, 5, 6],  # row 1
#     [7, 8, 9],  # row 2
#     [0]         # row 3
# ]
# print(number_grid[0][0])

# for row in number_grid:
#     for col in row:
#         print(col)

# --------------------------------------------------------------------
# 15 - Build a Translator

# string change to another language
# vowels -> g
# e.g.   dog -> dgg, cat -> cgt

# def translator(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation += "G"
#             else:
#                 translation += "g"
#         else:
#             translation += letter
#     return translation

# print(translator(input("Enter a phrase: ")))

# --------------------------------------------------------------------
# 16 - Comments

'''
This is comment
Multiple line comment
'''
# This is also comment

# --------------------------------------------------------------------
# 17 - Try Except

# if something goes wrong this will catch that errors, handle them
# it is useful to protect program
# try:
#     value = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)

# except ValueError as err:
#     print("Invalid input")
# except ZeroDivisionError as err:
#    print(err)
# except:
#     print("Error appeared")

# --------------------------------------------------------------------
# 18 - Reading Files


