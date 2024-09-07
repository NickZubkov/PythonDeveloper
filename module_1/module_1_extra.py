grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
average_grades = []
for grade_list in grades:
    average_grades.append(sum(grade_list) / len(grade_list))
students_dict = dict(zip(students_list, average_grades))
print(students_dict)