"""
enigmaRotors.py

This module handles the configuration and setup of rotors and reflectors
in the Enigma Machine, including the selection of rotors and reflectors
based on user input.
"""

# Define rotor notches in a dictionary.
rotor_notches_dict = {
    "I": 17,  # Notch position for rotor I
    "II": 5,  # Notch position for rotor II
    "III": 22,  # Notch position for rotor III
    "IV": 9,  # Notch position for rotor IV
    "V": 25,  # Notch position for rotor V
    "Beta": 15,  # Notch position for rotor Beta
    "Gamma": 2,  # Notch position for rotor Gamma
}

def rotors_setup():
    """
    Prompts the user to select three rotors for the Enigma Machine.

    Returns:
        list: A list of tuples where each tuple contains the rotor name
              and its corresponding wiring configuration.
    """
    print("We are now going to check the rotor setup.")

    # Define the rotors in a dictionary with their labels
    rotors = {
        "Beta": "LEYJVCNIXWPBQMDRTAKZGFUHOS",
        "Gamma": "FSOKANUERHMBTIYCWLQPZXVGJD",
        "I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "IV": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "V": "VZBRGITYUPSDNHLXAWMJQOFECK",
    }

    # Show rotors available for selection
    print_rotors_to_choose(rotors)

    # Ask the user to input which rotors they want to use
    selected_rotors = []
    for i in range(3):  # Now we allow the user to pick 3 rotors
        while True:
            rotor_choice = input(
                f"Starting with the rightmost rotor being 1, please enter Rotor {i + 1} (e.g., 'I', 'II', 'III', 'IV', 'V', 'Beta', 'Gamma'): ").strip()

            # Special handling for Roman numerals: Keep them uppercase
            if rotor_choice.upper() in rotors:
                rotor_choice_normalized = rotor_choice.upper()
            else:
                # Normalize other names by capitalizing first letters
                rotor_choice_normalized = ' '.join(word.capitalize() for word in rotor_choice.split())

            if rotor_choice_normalized in rotors:
                selected_rotors.append((rotor_choice_normalized, rotors[rotor_choice_normalized]))
                break
            else:
                print("Invalid choice. Please select a valid rotor from the list.")

    print("\nRotors selected for today's setup:")
    for rotor in selected_rotors:
        print(f"{rotor[0]}: {rotor[1]}")

    return selected_rotors


def reflectors_setup():
    """
    Prompts the user to select a reflector for the Enigma Machine.

    Returns:
        tuple: A tuple containing the selected reflector name and its wiring.
    """
    print("We are now going to check the reflector setup.")

    reflectors = {
        "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
        "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    }
    print_reflectors_to_choose(reflectors)

    # Ask the user to input which reflector they want to use
    selected_reflector = None
    while True:
        reflector_choice = input("Please enter Reflector (e.g., 'A', 'B', 'C'): ").strip().upper()

        if reflector_choice in reflectors:
            selected_reflector = (reflector_choice, reflectors[reflector_choice])
            break
        else:
            print("Invalid choice. Please select a valid reflector from the list.")

    # Print the selected reflector
    print("\nReflector selected for today's setup:")
    print(f"{selected_reflector[0]}: {selected_reflector[1]}")

    return selected_reflector


def print_rotors_to_choose(rotors):
    """
    Prints the list of available rotors for the user to choose from.

    Args:
        rotors (dict): A dictionary of available rotors with their labels.
    """
    # Print out the list of available rotors in a simple format
    print("\nAvailable Rotors:")
    for rotor_name in rotors:
        print(f"- {rotor_name}")

def print_reflectors_to_choose(reflectors):
    """
    Prints the list of available reflectors for the user to choose from.

    Args:
        reflectors (dict): A dictionary of available reflectors with their labels.
    """
    # Print out the list of available rotors in a simple format
    print("\nAvailable Reflectors:")
    for reflector_name in reflectors:
        print(f"- {reflector_name}")

def ring_settings_setup(selected_rotors):
    """
    This function is defined but not yet implemented.
    It will handle the ring settings for the rotors.
    """
    """
    Prompts the user to enter the ring settings for each selected rotor.

    Args:
        selected_rotors (list): A list of tuples containing selected rotor names 
                                and their configurations.

    Returns:
        list: A list of integers representing the ring settings for each rotor.
    """
    ring_settings = []
    for rotor in selected_rotors:
        while True:
            ring_setting_input = input(f"Enter the ring setting for {rotor[0]} (0-25): ")
            try:
                ring_setting = int(ring_setting_input)
                if 0 <= ring_setting <= 25:
                    ring_settings.append(ring_setting)
                    break
                else:
                    print("Please enter a valid number between 0 and 25.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return ring_settings