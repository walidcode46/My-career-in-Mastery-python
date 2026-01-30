# --------------------------------------------------------
# ------- loops/loops.py ---------------------------------
# --------------------------------------------------------
# Loops Example: Printing Numbers from 1 to 5
# This program demonstrates two types of loops in Python: a for loop and a while loop.
# The for loop iterates over a range of numbers from 1 to 5 and prints each number.
# The while loop initializes a counter at 1 and continues to print the counter value
# until the counter exceeds 5, incrementing the counter by 1 in each iteration.
# --------------------------------------------------------

print("python 1")
print("python 2")
print("python 3")
print("python 4")
print("python 5\n")

counter = 1         # Initialize counter
while counter <= 5: # Loop until counter is greater than 5
    print(f'Python {counter}')  # Print the current counter value
    counter += 1    # Increment counter by 1
print("\nFinished")   # Print finished message   
