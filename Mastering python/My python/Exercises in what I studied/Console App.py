# --------------------------------------------------------
# --Exercises in what I studied/Console App.py--------------
# --------------------------------------------------------
# Console App Example: User Information and Status Check
# This program simulates a console application that collects user information,
# checks registration status, and evaluates age and income levels.
# --------------------------------------------------------

print("===============================================")
print("=== Welcome to Smart User Management System ===")
print("===============================================\n")

register = input("\nWould you like to register your information? (Yes/No): ")

user = register.lower() == "yes"
if user: 
    name = input("Please enter your name : ")
    age  = input("Please enter your age : ")
    city = input("Please enter your city : ")
    monthly_income = input("Please enter your monthly income : ")

    Variables = f"Name : {name}\n" f"age : {age}\n" f"city : {city} \n" f"monthly income : {monthly_income}"
    print("\n--- User Information ---")
    print(Variables)
    print("-----------------------------------------------")     
else:
    print("\nYou chose not to register. Exiting the application.\n")
    exit()
case_examination = float(age.split()[0])

if case_examination >=22:
    
    print("You are an adult\n")
elif case_examination <=21:
    print("You are young\n")

income = float(monthly_income.split()[0])

if income >=10000:
    print("Great income\n")
elif income <=5000:
    print("average income\n")
else:
    print("Low income\n")

