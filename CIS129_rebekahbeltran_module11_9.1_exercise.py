# 9.1
# CIS129
# rebekah beltran
# dec. 2024

with open('grades.txt', 'w') as file:

    while True:

        grade = input("Please enter a grade (or enter 'end' to quit): \n")

        if grade.lower() == 'end':

            break

        file.write(grade + '\n')
