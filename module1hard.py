grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортировка имен учеников по алфавиту
students = list(students)
res = students.sort()

# Нахождение среднего балла
for i in range(len(grades)):
    grades[i] = sum(grades[i])/len(grades[i])

# Составление словаря
gpa = dict(zip(students, grades))
print(gpa)
