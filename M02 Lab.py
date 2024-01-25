'''
program name: M02 Lab.py
Author: Bo Wang
Discription: A program that checks if a student is on the Dean's List or Honor Roll by entering their name and GPA.
'''

while True:
    # Getting user input and formatting
    last_name = input("Please enter your last name (enter ZZZ to quit): ").strip().title()
    if last_name.upper() == "ZZZ":
        break
    first_name = input("Please enter your first name: ").strip().title()

    # Getting user's GPA
    GPA = float(input("Please enter your GPA: "))

    # Checking for Dean's List and Honor Roll, and printing accordingly
    if GPA >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif GPA >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} has not made the Dean's List or Honor Roll.")