students_height = input("List of students height").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
#print(students_height)

total_heights = 0
for h in students_height:
    total_heights += h
total_students = 0
for s in students_height:
    total_students +=1
average_height =round(total_heights / total_students)
print(average_height)
