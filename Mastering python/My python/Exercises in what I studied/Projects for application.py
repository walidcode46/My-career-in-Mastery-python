# ------------------------------
# ----- quetions 3 ---------------
# ------------------------------
# Writing a program that asks the user about the name and surname
# Incorporating the name and surname into one string
# Print a welcome message using a newline \n
# Extract the first and last 3 letters of the noun 

print("whats your name ")
Name = input()
print("whats your surname")
Surname = input()
NS = Name + "\n" + Surname
print(f"welcom\n{NS}")

print(Name[2::]) # the first and last 3 letters of the noun 