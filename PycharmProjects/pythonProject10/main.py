students_height = input("List of students height").split()
for n in range(0, len(students_height)):
  students_height[n] = int(students_height[n])
print(students_height)
high_score = 0
for s in students_height:
    if s>high_score:
        high_score = s
print(f"The highest score is {high_score}")
