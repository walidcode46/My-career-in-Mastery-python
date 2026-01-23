# --------------------------------------------------------
# ------- Logical Operators/logical_operators.py -----------
# --------------------------------------------------------
# Logical Operators Example: All Players Want to Play Football
# This program checks if all players want to play football using the logical AND operator.
# If all players agree, it prints "Health and wellness"; otherwise, it prints "Everyone should play football".
# Input from five players
# Each player inputs 'yes' or 'no' to indicate if they want to play football.
# --------------------------------------------------------

hamza = input("Player 1 - Do you want to play football? (yes/no): ") # Player 1 input
yaser = input("Player 2 - Do you want to play football? (yes/no): ") # Player 2 input
walid = input("Player 3 - Do you want to play football? (yes/no): ") # Player 3 input
mohsin= input("Player 4 - Do you want to play football? (yes/no): ") # Player 4 input
jawad = input("Player 5 - Do you want to play football? (yes/no): ") # Player 5 input

playing_football1 = hamza.lower() == "yes" # Player 1 condition
playing_football2 = yaser.lower() == "yes" # Player 2 condition
playing_football3 = walid.lower() == "yes" # Player 3 condition
playing_football4 = mohsin.lower() == "yes" # Player 4 condition
playing_football5 = jawad.lower() == "yes" # Player 5 condition
if  playing_football1 and playing_football2 and playing_football3 and playing_football4 and playing_football5: # All players want to play football
    print("Health and wellness")            # Print if all players want to play football
else:                                       # Not all players want to play football
    print("Everyone should play football")  # Print if not all players want to play football