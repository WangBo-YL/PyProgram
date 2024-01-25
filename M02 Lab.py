'''
program name: M02 Lab.py
Author: Bo Wang
Discription: A program that checks if a student is on the Dean's List or Honor Roll by entering their name and GPA.
'''

while True:
    last_name = input("Please enter your last name: ")
    if last_name == "ZZZ":
        break
    first_name = input("Please enter your first name: ")
    GPA = float(input("Please enter your GPA: "))
    if GPA >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    elif GPA >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")
    else:
        print(first_name, last_name, "has not made the Dean's List or Honor Roll.")
