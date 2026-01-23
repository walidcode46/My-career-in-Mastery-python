# --------------------------------------------------------
# --Exercises in what I studied/FinancialStatusChecker.py-
# --------------------------------------------------------
# Financial Status Checker Example: Determine Financial Status Based on Money Input
# This program prompts the user to input their amount of money and categorizes
# their financial status as "rich", "poor", or "normal" based on predefined thresholds
# --------------------------------------------------------

print("===================================")

Money = float(input("How matshnmoney: "))

if Money > 1000:
    print("\nYou are a rish ")

elif Money < 400:
    print("\nYoo are poor ")    
else:
    print("You are a Normel")

print("===================================")
Money1 = float(input("How matsh money: "))

if Money1 > 100000:
    print("You are a rish")

elif Money1 < 40000:
    print("Yoo are poor ")    
else:
    print("You are a Normel")

print("===================================")