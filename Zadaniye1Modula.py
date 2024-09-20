grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students= {'Ilya', 'Kirill', 'Artur', 'Valera', 'Anton'}
average_grades = {}
for i, student in enumerate(students):
    average_grade = sum(grades[i]) / len(grades[i])
    average_grades[student] = average_grade
    for student, average_grade in average_grades.items():
        print(f'Средний балл ученика {student}: {average_grade}')