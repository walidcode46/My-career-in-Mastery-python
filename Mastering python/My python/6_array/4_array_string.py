# -------------------------------------------
# ---- Reversing Strings In An Array -------
# -------------------------------------------
# Examples

name = "walid", "Jamal" # strings in an array
for reversing in range(0,2): # looping through the array
    print(name[reversing][0::2]) # reversing each string in the array

"""
| print(name[wel][0::2]) | is
    reversing each string in the array 
        by accessing each string using its
        index and slicing it with a step of 2 
     to get every second character.

Output:
wld
jml     
"""