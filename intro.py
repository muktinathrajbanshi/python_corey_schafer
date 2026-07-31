# import my_module as mm
from my_module import find_index, test

courses = ["History", "Math", "Physics", "Chemistry"]

# index = mm.find_index(courses, "Math")
index = find_index(courses, "Math")

print(index)
print(test)