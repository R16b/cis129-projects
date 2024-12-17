# 9.3
# CIS129
# rebekah beltran
# dec. 2024

import csv

def calculate_average(exam1, exam2, exam3):

    return (exam1 + exam2 + exam3) / 3


with open('grades.csv', 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile)


    while True:

        first_name = input("Please enter a first name (or enter 'q' to quit): \n")
        if first_name == 'q':
            break

        last_name = input('Please enter a last name: \n')

        exam1 = int(input('Enter grade from exam 1: \n'))

        exam2 = int(input('Enter grade from exam 2: \n'))

        exam3 = int(input('Enter grade from exam 3: \n'))


        csvwriter.writerow([first_name, last_name, exam1, exam2, exam3])
