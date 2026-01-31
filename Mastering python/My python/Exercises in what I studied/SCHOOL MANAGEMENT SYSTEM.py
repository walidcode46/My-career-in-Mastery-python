# ------------------------------------------------------------------
# --- PROJECT: SCHOOL MANAGEMENT SYSTEM (LEVEL 1) ---------------
# ------------------------------------------------------------------
# --- OBJECTIVE: Create a simple school management system that
# --- collects student information, calculates grades, and displays
# --- relevant details.
# ------------------------------------------------------------------

# --- FUNCTION TO GREET USER
def greet_user(first_Name, Last_Name):
    """Function to return a welcome message."""
    message = f"\nWe welcome you to our School Management System, {first_Name} {Last_Name}!\n"
    return message 
    
# greet_user("Student")
def display_project_info():
    print("==========================================================")
    print("==== PROJECT: SCHOOL MANAGEMENT SYSTEM (LEVEL 1) =========")
    print("==========================================================\n")
    
    print("-----------------------------------------------------------") 

    first_Name = input("What is your Name : ")
    Last_Name  = input("What is your Last Name : ")
    Level      = input("What is your Level : ") 

    print(greet_user(first_Name, Last_Name))

    print("-----------------------------------------------------------")
    Full_Name =f" Your Name is {first_Name.upper()}\n Your Lanst Name is {Last_Name.upper()}\n Your Age is {Level.upper()}"
    print(Full_Name) 

    print("-----------------------------------------------------------")

    User = float(input("How Old Are You ?\n > "))

    if User >= 18 :
        print("You Are in Adult") 
    elif User <= 15 :
        print("You Are in Minor") 
    else:
        print("Eligible for CS Club") 

    grades = [10, 15, 20, 17, 18, 19]
    total = 0 
    min_grade = grades[0]
    print("-----------------------------------------------------------")

    print("Students' grades :")
    for index in range(len(grades)):
        print(f"> {grades[index]}")

    print("-----------------------------------------------------------")

    print("Total student grades :")
    for T in grades:
        total = total + T
        print(f"> {total} ") 
            
    print("-----------------------------------------------------------")

    print("Greater Justice :")  
    for min in grades:
        if min > min_grade:
            min_grade = min

    print(f"> {min_grade}")

    print("-----------------------------------------------------------") 

    print("Lesser Justice : ") 
    for min2 in grades:
        if min2 < min_grade:
            min_grade = min2

    print(f"> {min_grade}") 

    print("-----------------------------------------------------------")  
# CALL THE FUNCTION TO DISPLAY PROJECT INFO
display_project_info()


