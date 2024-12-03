grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_list = sorted(list(students))
avg_grade_by_student = dict()

student_count = len(students)
for i in range(student_count):
    grade = sum(grades[i])/len(grades[i])
    avg_grade_by_student[student_list[i]] = grade

print(avg_grade_by_student)
