# ================================
#       PERSONAL PROFILE APP
# ================================
# This is a simple Python program that collects personal information
# from the user and displays it in a formatted profile summary.
# Users can input their full name, age, city, job, and hobby.
# The program also displays the first letter of the name,
# the last letter of the city, and the data type of the age input.
# ================================

print("===============================")
print("       PERSONAL PROFILE      ")
print("===============================")

print("-------------------------------")
# Collecting user input for personal details
Name  = input("Full Name : ")  # User's full name
Age   = input("Age       : ")  # User's age
City  = input("City      : ")  # User's city
Job   = input("Job       : ")  # User's job or profession
Hobby = input("Hobby     : ")  # User's favorite hobby
print("-------------------------------")

print("=== YOUR ABOUT ===")
# Displaying the formatted personal profile
print(f"About Me : Hi, I'm {Name}, I'm {Age} Years old, I live in {City}, and I love {Hobby}")
print(f"First Letter of Name: {Name[0]}") # Extracting the first character of the name
print(f"Last Letter of City: {City[-1]}") # Extracting the last character of the city
print(type(Age))  # Showing the data type of the Age variable
print("===============================")  
