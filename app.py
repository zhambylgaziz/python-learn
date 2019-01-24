# Python lessons

# using Learn Python - Full Course for Beginners from freeCodeCamp.org
# https://youtu.be/rfscVS0vtbw

# --------------------------------------------------------------------
# 1 - String & Integer

#char_name = "Zhambyl"
#char_age = 19
#print("Hello, my name is "+char_name+", and I'm", char_age, "y.o")

# --------------------------------------------------------------------
# 2 - List

# can store any of data types
# array
#friends = ["Ammyy", "Jammy", "Gabby"]
#           0(-3)    1(-2)    2(-1)
#print(friends[-3])
#friends[1] = "Jimmy"
#print(friends[1:])

# --------------------------------------------------------------------
# 3 - List functions

#numbers = [4, 7, 14, 21 ,42]
#friends = ["Ammyy", "Jammy", "Gabby", "Jammy", "Kobby", "Tobby"]
#friends.extend(numbers) #add 2 lists together
#friends.append("Funny") #add 1 item to the end
#friends.insert(1, "Zeddy") #add item to chosen position
#friends.remove(14) #remove 1 item
#friends.clear(); #empty list
#friends.pop() #removes last item
#print(friends.index("Gabby")) #return item's index
#print(friends.count("Jammy")) #counts item
#friends.sort()  #sort by alphabetic order
#friends2 = friends.copy().reverse() #copies to friends2 and reverse it
#print(friends)

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
# 9 -
















