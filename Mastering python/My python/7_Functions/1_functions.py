# --------------------------------------------------------
# ------- Functions/functions.py --------------------------
# --------------------------------------------------------
# Functions Example: Employee Salary Calculation and Message Printing
# This program defines two functions: one for calculating an employee's salary
# based on a base salary, bonus, and credit; and another for printing a message
# in a formatted way. It demonstrates the use of functions in Python.
# --------------------------------------------------------

# Function that calculates the employee's salary
# base salary = 5000
# bonus: extra money added
# credit: money deducted
def employee_salary(bonus=0, credit=0):
    return 5000 + bonus - credit


# Calculating salaries for different employees
employee1 = employee_salary(100)   # Employee with 100 bonus
employee2 = employee_salary(200)   # Employee with 200 bonus
employee3 = employee_salary(300)   # Employee with 300 bonus
employee4 = employee_salary(0)     # Employee with no bonus

# Printing all salaries
print(employee1, employee2, employee3, employee4)


# Function that prints a message in a simple format
def message(text):
    print("The message:")   # Title
    print(text)             # The actual message
    print("End")            # End of message


# Calling the message function with a text
message("hy there welcome to python functions")
