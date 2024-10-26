from EnigmaMachine.ui.welcome import typing_welcome_message, ask_for_instructions
from EnigmaMachine.core.enigmaPlugs import get_user_leads
from EnigmaMachine.core.enigmaRotors import rotor_notches_dict, rotors_setup, reflectors_setup
from EnigmaMachine.ui.chooseMode import choose_mode_and_encode

#Call the welcome message functions
if __name__ == "__main__":
    """
    enigma.py
    Entry point for the Enigma Machine simulation. This script manages user interactions
    and orchestrates the encoding process using selected rotors, reflectors, and plugboard settings.
    """
    # Display welcome messages.
    typing_welcome_message()

    # Add an empty line after the image
    print()

    # Ask if the user needs detailed instructions.
    ask_for_instructions()

    # Set up today's plugboard based on user input.
    plugboard = get_user_leads()

    # Add an empty line after the image.
    print()

    # Select rotors for encoding; returns a list of tuples with rotor names and their settings.
    selected_rotors = rotors_setup()

    # Check if any rotors were selected; exit if none are chosen.
    if not selected_rotors:
        print("No rotors were selected. Please select at least one rotor to proceed.")
        exit(1)  # Exit or handle the error as needed.

    # Set up reflectors; get the reflector set up.
    selected_reflector = reflectors_setup() # Get the reflector set up

    print("Now we're all set up, it's time to start encoding")

    # Rotor positions; starting positions for the rotors.
    rotor_positions = [0, 0, 0]

    # Ring settings; assuming no initial offset (A aligned with A).
    ring_settings = [0, 0, 0]

    # NOTE: The ring settings functionality has been written but is not yet implemented.
    # Uncomment the following line to prompt the user for ring settings once implemented.
    # ring_settings = ring_settings_setup(selected_rotors)

    # Handle user choice for input mode and encoding.
    choose_mode_and_encode(plugboard, selected_rotors, selected_reflector, rotor_positions, rotor_notches_dict,
                           ring_settings)
