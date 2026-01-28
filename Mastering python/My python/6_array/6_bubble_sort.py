# -----------------------------------------------
# ---- Bubble Sort Algorithm in Python ----------
# -----------------------------------------------
# This program implements the bubble sort algorithm to sort a list of numbers in ascending order.
# It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in
# the wrong order. The process is repeated until the list is sorted.
# -----------------------------------------------

grades = [10 , 2, 33, 45, 9, 6, 3, 7, 1] # Initial unsorted list

print(grades) # Print the unsorted list
length = len(grades) # Get the length of the list

for i in range(length): # Outer loop to ensure all elements are sorted
    for index in range(0, length -1): # Inner loop to compare adjacent elements
        first  =  grades[index]       # Current element
        second = grades[index +1]     # Next element
        if first > second:            # If current element is greater than next element
            grades[index] = second    # Swap elements
            grades[index +1] = first  # Swap elements

print(grades)  # Print the sorted list