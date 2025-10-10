# ================================
#        PERSONAL PROFILE
# ================================
# Full Name : Walid Amrani
# Age       : 18
# City      : Casablanca
# Job       : Student
# Hobby     : Football
# -------------------------------
# About me  : Hi, I'm Walid Amrani, I'm 18 years old, I live in Casablanca, and I love Football.
# First Letter of Name: W
# Last Letter of City: a
# Data Type of Age: <class 'str'>
# ================================

print("===============================")
print("       PERSONAL PROFILE      ")
print("===============================")
Name  = input("Full Name : ")
Age   = input("Age       : ")
City  = input("City      : ")
Job   = input("Job       : ") 
Hobby = input("Hobby     : ")
print("-------------------------------")
print("\n=== YOUR ABOUT ===")
print(f"About Me : Hi, I'm {Name}, I'm {Age} Years old, I live in {City}, and I love {Hobby}")
print(f"First Letter of Name: {Name[0]}")
print(f"Last Letter of City: {City[-1]}")
print(type(Age))
print("===============================") 