# --------------------------------------------------------
# ------- TextRepeater.py ---------------------------------
# --------------------------------------------------------
# Text Repeater Example: Repeat User Input Multiple Times
# This program asks the user if they want to repeat a specific text multiple times.
# If the user agrees, it prompts for the text and the number of repetitions,
# then prints the text the specified number of times using a while loop.
# --------------------------------------------------------

# Ask the user if they want to repeat something
repeat_question = input("Do you want to repeat something multiple times? (yes/no): ").strip() 
def lm3awda():
    repeat_question2 = input(" wach baghi tatba3 chi silsila dyal lear9am katbda f 0 wekatsali fra9m li bghiti (yes/no)")

    wants_to_repeat_int =  repeat_question2 == "yes"
    if wants_to_repeat_int:
            print("What would you like to repeat?")
            text_to_repeat_int = int(input("> "))
            print(f"How many times do you want to repeat '{text_to_repeat_int}'?")
#             repeat_count_int = int(input("> "))

            print(f"\nOkay! Here is '{text_to_repeat_int}' repeated {repeat_count_int} times:\n")
# Convert the answer to boolean
# wants_to_repeat = repeat_question == "yes"

if repeat_question == "yes":
    print("What would you like to repeat?")
    text_to_repeat = int(input("> "))

    print(f"How many times do you want to repeat '{text_to_repeat}'?")
    repeat_count = int(input("> "))

    print(f"\nOkay! Here is '{text_to_repeat}' repeated {repeat_count} times:\n")

    counter = 1
    while counter <= text_to_repeat:
            print(text_to_repeat)
            counter += 1

    print("\nFinished.")
else:
    print("Okay, no repetition needed.") 
