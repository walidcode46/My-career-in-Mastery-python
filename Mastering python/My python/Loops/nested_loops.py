# --------------------------------------------------------
# ------- loops/nested_loops.py --------------------------
# --------------------------------------------------------  
# Nested Loops Example: Iterating Over Two Ranges
# The outer loop iterates 5 times, and for each iteration of the outer loop,
# the inner loop iterates 3 times, printing the current values of both loop variables.
# This demonstrates the concept of nested loops in Python.
# --------------------------------------------------------

for x in range(5):          # Outer loop iterating 5 times
    for y in range(3):      # Inner loop iterating 3 times
        print(f"X: {x}, Y: {y}")  # Print current values of x and y