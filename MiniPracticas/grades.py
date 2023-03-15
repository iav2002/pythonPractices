student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

#TODO-2: Manipulacion de Cambion de valores en un hashmap.👇
for student in student_scores:
    score = student_scores[student]
    if score  > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else: 
         student_grades[student] = "Fail"
print(student_grades)