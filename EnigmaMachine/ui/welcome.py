import time

"""
welcome.py
This module handles the welcome messages and instructions for the Enigma Machine simulation.
It provides a visual welcome message and prompts users for instructions.
"""

def typing_welcome_message():
    """Displays a welcome message with a typing effect."""
    message = """
          ________________
         |                |
         |  ENIGMA        |
         |    MACHINE     |
         |________________|
           /  |      |  \\
          /   |      |   \\
         /____|______|____\\
        |______o______o____|
    """
    print("Welcome to the Enigma Machine!\n")
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.02)  # Delay between each character

def ask_for_instructions():
    """Prompts the user for detailed instructions and displays them if requested."""
    while True:
        response = input("First we are going to enter the Plug Leads. Would you like detailed instructions? (yes/no): ").strip().lower()
        if response == "yes":
            detailed_instructions()
            break
        elif response == "no":
            print("Okay, let's proceed!\n")
            break
        else:
            print("Please enter 'yes' or 'no'.")


def detailed_instructions():
    instructions = """
    Detailed Instructions:
    1. You will be asked to enter 10 plug leads (pairs of letters).
    2. Each plug lead consists of two unique uppercase letters (e.g., 'AB').
    3. You cannot use the same letter twice across all leads.
    4. Letters should be entered without any quotes or special characters e.g. AB
    5. You will be shown the leads you entered for today once you have entered them. Please double check your entries.
    6. If you are unsure, speak to your supervisor.
    """
    print(instructions)

