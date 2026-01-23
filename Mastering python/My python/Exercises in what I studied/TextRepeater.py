# --------------------------------------------------------
# ------- TextRepeater.py ---------------------------------
# --------------------------------------------------------
# Text Repeater Example: Repeat User Input Multiple Times
# This program asks the user if they want to repeat a specific text multiple times.
# If the user agrees, it prompts for the text and the number of repetitions,
# then prints the text the specified number of times using a while loop.
# --------------------------------------------------------

# Ask the user if they want to repeat something
repeat_question = input("Do you want to repeat something multiple times? (yes/no): "+"").strip() 

# Convert the answer to boolean
wants_to_repeat = repeat_question == "yes"

if wants_to_repeat:
    print("What would you like to repeat?")
    text_to_repeat = input(">")

    print(f"How many times do you want to repeat '{text_to_repeat}'?")
    repeat_count = int(input("> "))

    print(f"\nOkay! Here is '{text_to_repeat}' repeated {repeat_count} times:\n")

    counter = 1
    while counter <= repeat_count:
        print(text_to_repeat)
        counter += 1

    print("\nFinished.")
else:
    print("Okay, no repetition needed.")
