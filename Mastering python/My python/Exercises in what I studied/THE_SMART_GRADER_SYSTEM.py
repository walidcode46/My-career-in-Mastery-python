# -----------------------------------------------------------
# ----------- THE SMART GRADER SYSTEM -----------------------
# -----------------------------------------------------------
# This project is designed to manage student grades,
# calculate averages, and sort grades using basic programming concepts.
# -----------------------------------------------------------

print("===========================================================")
print("=== Welcome to THE SMART GRADER SYSTEM ===")
print("===========================================================\n")

# Function to calculate average
def get_average(total, count): 
    """Function to calculate average.""" 
    return total / count 

print("-----------------------------------------------------------") 
# User Information Input
first_Name = input("Please enter your First Name : ")
Last_Name  = input("Please enter your Last Name : ")
Full_Name = f"{first_Name} {Last_Name}"
print(f"\nYour Full Name in UPPERCASE is: {Full_Name.upper()}")

print("-----------------------------------------------------------")
# Age Verification
age = int(input("Please enter your Age : "))
if age >= 12 and age <= 18:
    print("Welcome High School Student\n")
else: 
    print("Welcome Student\n") 

print("-----------------------------------------------------------") 
# Grade Input and Processing
student_grades = []
for Grde in range(5):
    grade = float(input(f"Please enter grade {Grde + 1}: "))
    student_grades.append(grade) 
total = 0
for grade in student_grades:
    total += grade 
average = get_average(total, len(student_grades)) 

print("-----------------------------------------------------------")
# Bubble Sort 
n = len(student_grades)
for i in range(n):
    for j in range(0, n-i-1):
        if student_grades[j] > student_grades[j+1]:
            student_grades[j], student_grades[j+1] = student_grades[j+1], student_grades[j]
print(f"Your Average Grade is: {average}")
print(f"Your Sorted Grades are: {student_grades}")

print("-----------------------------------------------------------")
print("=== Thank you for using THE SMART GRADER SYSTEM ===")
print("===========================================================")

# END OF THE SMART GRADER SYSTEM
