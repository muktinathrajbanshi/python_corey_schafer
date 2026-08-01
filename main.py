# message = "Hello World"
# message = 'bobby\'s World'
# # message = "bobby's World"
# message = """bobby's World was a good
# cartoon in the 1990s"""
from email import message

# message = "Hello World"

# print(len(message))
# print(message[0:5])
# print(message[:5])
# print(message[6:])

# print(message)

# message = "Hello World"
# print(message.lower())
# print(message.upper())
# print(message.count("Hello"))
# print(message.count("l"))
# print(message.find("World"))
# print(message.find("universe"))

# message = "Hello World"
# message = message.replace("World", "Universe")
# print(message)

greeting = "Hello"
name = "Michael"

# message = greeting + ", " + name
# message = greeting + ", " + name + ". Welcome!"
# message = "{}, {}. Welcome!".format(greeting, name)

# message = f"{greeting}, {name.upper()}. Welcome!"

# print(dir(name))
# print(help(str))
# print(help(str.lower))

# Integers and Floats
# num = 3
# # num = 3.4
# print(type(num))

# Arithmetic Operators:
# Addition: 3 + 2
# Subtraction: 3 - 2
# Multiplication: 3 * 2
# Division: 3 / 2
# Floor Division: 3 // 2
# Exponent: 3 ** 2
# Modulus: 3 % 2

# print(3 * (2 + 1))
#
# num = 1
# num *= 10
# print(num)

# print(abs(-3))
# print(round(3.75, 1))

# Comparisons:
# Equal: 3 == 2
# num_1 = 3
# num_2 = 2
#
# print(num_1 == num_2)

# Not Equal: 3 != 2
# num_1 = 3
# num_2 = 2
#
# print(num_1 != num_2)
# Greater Than: 3 > 2
# num_1 = 3
# num_2 = 2
#
# print(num_1 > num_2)
# Less Than: 3 < 2
# num_1 = 3
# num_2 = 2
#
# print(num_1 < num_2)
# Greater or Equal: 3 >= 2
# num_1 = 3
# num_2 = 2
#
# print(num_1 >= num_2)
# Less or Equal: 3 <= 2
# num_1 = 3
# num_2 = 2
#
# print(num_1 <= num_2)

# num_1 = "100"
# num_2 = "200"
#
# num_1 = int(num_1)
# num_2 = int(num_2)
#
# print((num_1 + num_2))

# Lists, Tuples, and Sets
# courses = ["History", "Math", "Physics", "Chemistry"]

# print(courses)
# print(len(courses))
# print(courses[-1])
# print(courses[0:2])
# print(courses[2:])

# courses = ["History", "Math", "Physics", "Chemistry"]
# courses_2 = ["Art", "Education"]



# courses.append("Computer Science")
# courses.insert(0,"Computer Science")
# courses.insert(0, courses_2)
# courses.extend(courses_2)
# courses.append(courses_2)

# courses.remove("Math")
# courses.pop()
# popped = courses.pop()
# print(popped)

# courses = ["History", "Math", "Physics", "Chemistry"]
# nums = [1, 5, 2, 4, 3]
# courses.reverse()
# courses.sort()
# nums.sort()
#
# courses.sort(reverse=True)
# nums.sort(reverse=True)

# sorted_courses = sorted(courses)

# print(sorted_courses)
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# courses = ["History", "Math", "Physics", "Chemistry"]

# for course in courses:
#     print(course)

# for index, course in enumerate(courses, start=1):
#     print(index, course)


# print(courses.index("Art"))
# print("Math" in courses)

# courses = ["History", "Math", "Physics", "Chemistry"]
#
# course_str = " - ".join(courses)
#
# new_list = course_str.split(" - ")
#
# print(course_str)
# print(new_list)

# Mutable
# list_1 = ["History", "Math", "Physics", "Chemistry"]
# list_2 = list_1
#
# print(list_1)
# print(list_2)
#
# list_1[0] = "Art"
#
# print(list_1)
# print(list_2)

# Tuples
# Immutable
# tuple_1 = ["History", "Math", "Physics", "CompSci"]
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0] = "Art"
#
# print(tuple_1)
# print(tuple_2)

# Sets
# cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
# art_courses = {"History", "Math", "Art", "Design"}

# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))

# Empty Lists
# empty_list = []
# empty_list = list()

# Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# Empty Sets
# empty_set = {} # This isn't right! It's a dict
# empty_set = set()

# Dictionaries
# student = {"name" : "Michael", "age" : 25, "courses": ["Math", "CompSci"]}

# age = student.pop("age")
# del student["age"]
# student.update({"name": "Jane", "age" : 26, "phone": "555-5555"})
# student["phone"] = "555-5555"
# student["name"] = "Jane"

# print(student.get("phone", "Not Found"))
# print(student)
# print(age)

# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student:
# for key, value in student.items():
    # print(key, value)

# Conditionals and Booleans - If, Else, and Elif Statements
# Comparisons:
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=
# Object Identity: is

# and
# or
# not

# user = "Admin"
# logged_in = False

# if user == "Admin" or logged_in:
#     print("Admin Page")
# if not logged_in:
#     print("Please log in")
# else:
#     print("Welcome")
#
# a = [1, 2, 3]
# b = a
# b = [1, 2, 3]
#
# print(id(a))
# print(id(b))
# print(a is b)
# print(a == b)
# print(id(a) == id(b))

# False Values:
#     False
#     None
#     Zero of any numeric type
#     Any empty sequence. For example, "", (), [].
#     Any empty mapping. For example, {}.

# condition = False
# condition = None

# condition = "Test"
#
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")





# if True:
#     print("Conditional was True")

# language = "Java"
#
# if language == "Python":
#     print("Language is Python")
# elif language == "Java":
#     print("Language is Java")
# elif language == "JavaScript":
#     print("Language is JavaScript")
# else:
#     print("No match")

# Loops and Iterations - For/While Loops
# nums = [1, 2, 3, 4, 5]
#
# for num in nums:
#     print(num)

#
# nums = [1, 2, 3, 4, 5]
#
# for num in nums:
#     if num == 3:
#         print("Found")
#         break
#     print(num)

#
# nums = [1, 2, 3, 4, 5]
#
# for num in nums:
#     if num == 3:
#         print("Found")
#         continue
#     print(num)


# nums = [1, 2, 3, 4, 5]
#
# for num in nums:
#     for letter in "abc":
#         print(num, letter)

# for i in range(1, 11):
#     print(i)
#
# x = 0
# while x < 10:
#     print(x)
#     x += 1

#
# x = 0
# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1


# x = 0
# while True:
    # if x == 5:
    #     break
    # print(x)
    # x += 1

# Functions
# def hello_func():
    # pass
    # print("Hello Function!")

# hello_func()
# print("Hello Function.")
# print("Hello Function.")
# print("Hello Function.")
# print("Hello Function.")

# def hello_func():
#     print("Hello Function.")
#
# hello_func()
# hello_func()
# hello_func()
# hello_func()
#DRY

# def hello_func(greeting):
#     return "{} Function.".format(greeting)
#
# print(hello_func("Hi"))
# print(hello_func().upper())
# print(len("Test"))

# def hello_func(greeting, name="you"):
#     return "{}, {}".format(greeting, name)
#
# print(hello_func("Hi"))

# def hello_func(greeting, name="you"):
    # return "{}, {}".format(greeting, name)

# print(hello_func("Hi", name="Muktinath  "))

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# student_info("Math", "Art", name="Muktinath", age=25)

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# courses = ["Math", "Art"]
# info = {"name": "Muktinath", "age": 25}
#
# student_info(courses, info)


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ["Math", "Art"]
# info = {"name": "Muktinath", "age": 25}

# student_info(*courses, **info)

# Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# def is_leap(year):
#     # Return True for leap years, False for non-leap years.
#
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# def days_in_month(year, month):
#     # Return number of days in that month in that year.
#
#     # year 2017
#     # month 2
#     if not 1 <= month <= 12:
#         return "Invalid month"
#
#     if month == 2 and is_leap(year):
#         return 29
#
#     return month_days[month]
#
# # print(is_leap(2020))
# print(days_in_month(2017, 2))

 # OS Module
# import os
#
# # print(dir(os))
# print(os.getcwd())
#
# os.chdir("C:/Users/ACER/Desktop")
#
# print(os.getcwd())

# import os
# from datetime import datetime

# os.chdir("C:/Users/ACER/Desktop")

# os.mkdir("Kurakani/Sub-Dir-1")
# os.makedirs("Kurakani/Sub-Dir-1")

# os.removedirs("Chat/Sub-Dir-1")

# os.rename("Kurakani", "Chat")
# print(os.getcwd())

# mod_time = os.stat("intro.py").st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.listdir())


import os
from datetime import datetime

os.chdir("C:/Users/ACER/Desktop")
for dirpath, dirnames, filenames in os.walk("C:/Users/ACER/Desktop"):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
