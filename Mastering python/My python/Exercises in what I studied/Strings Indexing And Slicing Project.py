# ------------------------------
# --- Question 4 ---------------
# ------------------------------
# Ask the user to enter any text
# Print the first 5 characters of the text
# Print the last 5 characters of the text
# Print every second character of the text
# Use \n to separate each output on a new line

print("enter any text") 
Text = input()
print(
    "the first 5 characters of the text:", Text[0:5], 
    "\nthe last 5 characters of the text:", Text[-5:], 
    "\nevery second character of the text:", Text[0::2]
)

