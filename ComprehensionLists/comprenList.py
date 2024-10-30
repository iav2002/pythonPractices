list = [1,2,3,4,5]
#de manera simple para poder entender el sistema

new_list = [n + 1 for n in list]
print(new_list)
#Same can be applied for a Strings

name = "Nacho"
letters_list = [letter for letter in name]
print(letters_list)

#multiplos de dos en un rango
range_list = [num * 2 for num in range(1,5)]
print(range_list)

# names = ["alex", "Beth", "Caroline", "Dave","Elanor"]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 5]

# # print(names)
# print(short_names)
# print(long_names)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
print(numbers)

import random 

names = ["alex", "Beth", "Caroline", "Dave","Elanor"]
students_scores = { student : random.randint(1,100) for student in names }
print(students_scores)

passed_students = {student: scores for (student,scores) in students_scores.items() if scores >=60 }
print(passed_students)