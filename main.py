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
tuple_1 = ["History", "Math", "Physics", "CompSci"]
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = "Art"

print(tuple_1)
print(tuple_2)





















