# ------------------------------
# ---The project 2----------------
# ------------------------------
# Ask the User For: full Name, age, city, hobby 
# Combine them into a formatted card using newline
# Extract the first and last 2 letters of the name 
# Extract the firt 3 letters of the city

# User information request
print("whats your full name ")
FullName = input()
print("whats your age")
Age = input()
print("whats your city")
City = input()
print("whats your hobby")
Hobby = input()
# Combine into a formatted card
Card = f"Name: {FullName}\nAge: {Age}\nCity: {City}\nHobby: {Hobby}"
print("Here is your personal info card:\n")
print(Card)
# Extracting specific letters
FirstLast2 = FullName[:2] + FullName[-2:]
First3City = City[:3]
print(f"First and last 2 letters of your name: {FirstLast2}")
print(f"First 3 letters of your city: {First3City}")
# Extract the first and last 3 letters of the noun
print(FullName[2::]) # the first and last 3 letters of the noun
