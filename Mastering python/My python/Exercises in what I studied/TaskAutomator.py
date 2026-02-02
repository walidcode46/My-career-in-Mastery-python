# ---------------------------------------------------------
# -- Multipurpose Tool: Text Repeater and Dynamic Counter -
# ---------------------------------------------------------
# This tool allows users to either repeat a given text multiple times
# or count from a specified start point to an end point, handling both
# incremental and decremental counting.
# Created by: [Your Name/Handle]
# Version: 1.0.0
# ---------------------------------------------------------

def run_multipurpose_tool():
    def run_text_repeater():

        user_choice = input("Do you want to repeat something multiple times? (yes/no): ").strip().lower().replace(" ", "")

        if user_choice == "yes":
            print("What would you like to repeat?")
            text_to_repeat = input("> ")
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

    run_text_repeater()
    # --------------------------------------------------------
    def dynamic_counter():
        # Asking the user if they want to start the counting process
        counting_decision = input("\nDo you want to start counting from a specific range? (yes/no): ").strip().lower().replace(" ", "")

        if counting_decision == "yes":
            print("Where do you want to start?")
            start_point = int(input("> "))

            print("Where do you want to end?")
            end_point = int(input("> "))

            print(f"\nOkay! Starting from '{start_point}' and ending at '{end_point}':\n")
            
            # Logic to handle both counting up and counting down
            if start_point <= end_point:
                # Counting Up (Incremental)
                for number in range(start_point, end_point + 1):
                    print(number)
            else:
                # Counting Down (Decremental)
                for number in range(start_point, end_point - 1, -1):
                    print(number)
                    
            print("\nFinished.")
        else:
            print("Okay, no counting needed.")

    # Execute the function
    dynamic_counter() 
 
run_multipurpose_tool()

