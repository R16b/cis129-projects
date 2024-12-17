# 9.2
# CIS129
# rebekah beltran
# dec. 2024

with open('grades.txt',  'r') as file:

    grades = file.read().splitlines()
    grades = [float(grade) for grade in grades]

    print('The individual grades: \n', grades)

    total = sum(grades)
    count = len(grades)
    average = total / count

    print('Total: ', total)
    print('Count: ', count)
    print('Average ', average)
