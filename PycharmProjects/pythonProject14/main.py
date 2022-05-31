students_score = {
    "harry": 81,
    "Ron":78,
    "Steve":99,
    "Cynthia":74
}
students_grade = {}

for student in students_score:
    score = students_score[student]
    if score>90:
        students_grade[student] = "Outstanding"
    elif score>80:
        students_grade[student] = "Exceedes expectation"
    elif score>70:
        students_grade[student] = "Acceptable"
    else:
        students_grade[student] = "Fail"

print(students_grade)
