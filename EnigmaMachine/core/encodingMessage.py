"""
encodingMessage.py
--------------------
This module contains functions for encoding messages using the Enigma machine's mechanism,
including rotor advancement and detailed step logging for each letter encoded.
"""

MAX_MESSAGE_LENGTH = 250  # Limit for the maximum length of the message

def update_rotor_positions(rotor_positions, rotor_notches_dict, selected_rotors):
    """
    Updates the rotor positions based on the current rotor settings
    and the notches defined in the rotor notches dictionary.

    Args:
        rotor_positions (list): A list representing the current positions of the rotors.
        rotor_notches_dict (dict): A dictionary mapping rotor names to their notch positions.
        selected_rotors (list): A list of selected rotors for the encoding process.

    Returns:
        list: The updated list of rotor positions after stepping.
    """
    for i in range(len(rotor_positions)):
        rotor_positions[i] = (rotor_positions[i] + 1) % 26  # Increment rotor position
        if rotor_positions[i] == rotor_notches_dict[selected_rotors[i][0]]:
            if i + 1 < len(rotor_positions):
                rotor_positions[i + 1] = (rotor_positions[i + 1] + 1) % 26  # Advance next rotor
    return rotor_positions

def advance_rotors(rotor_positions, rotor_notches):
    """
    Advances the rotors, simulating the stepping mechanism.
    Rightmost rotor steps by 1 on every keypress.
    Rotor 2 steps when rotor 1 reaches a certain notch.
    Rotor 3 steps when rotor 2 reaches a certain notch.
    """
    # Step rotor 1
    rotor_positions[0] = (rotor_positions[0] + 1) % 26

    # Check if rotor 1 hits the notch, advance rotor 2
    if rotor_positions[0] == rotor_notches.get(0, None):
        rotor_positions[1] = (rotor_positions[1] + 1) % 26

        # If rotor 2 hits the notch, advance rotor 3
        if rotor_positions[1] == rotor_notches.get(1, None):
            rotor_positions[2] = (rotor_positions[2] + 1) % 26


def encode_letter_with_rotor_advance(plugboard, selected_rotors, selected_reflector, letter, rotor_positions, rotor_notches):
    """
    Encode a single letter with rotor advancement and show detailed encryption steps.
    """
    """
    Encodes a single letter while advancing the rotors and showing detailed encryption steps.

    Args:
        plugboard (Plugboard): The plugboard instance for initial and final character transformations.
        selected_rotors (list): The list of selected rotors with their mappings.
        selected_reflector (tuple): The selected reflector's name and mapping.
        letter (str): The letter to be encoded.
        rotor_positions (list): The current positions of the rotors.
        rotor_notches (list): The notch positions for the selected rotors.

    Returns:
        str: The encoded letter after passing through the plugboard, rotors, reflector, and back.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    original_letter = letter  # Store the original letter for displaying later

    # Step 1: Plugboard input
    plugboard_input = plugboard.transform_character(letter)

    # Display rotor positions before encoding
    rotor_position_str = ''.join([alphabet[pos] for pos in rotor_positions])

    print(f"Keyboard Input: {original_letter}")
    print(f"Rotors Position: {rotor_position_str}")
    print(f"Plugboard Encryption: {plugboard_input}")

    # Step 2: Pass through rotors (with advancement)

    # Rotor 1
    rotor1_mapping = selected_rotors[0][1]
    index = (alphabet.index(plugboard_input) + rotor_positions[0]) % 26
    letter = rotor1_mapping[index]
    print(f"Wheel 3 Encryption: {letter}")

    # Rotor 2
    rotor2_mapping = selected_rotors[1][1]
    index = (alphabet.index(letter) + rotor_positions[1]) % 26
    letter = rotor2_mapping[index]
    print(f"Wheel 2 Encryption: {letter}")

    # Rotor 3
    rotor3_mapping = selected_rotors[2][1]
    index = (alphabet.index(letter) + rotor_positions[2]) % 26
    letter = rotor3_mapping[index]
    print(f"Wheel 1 Encryption: {letter}")

    # Step 3: Reflector
    reflector_mapping = selected_reflector[1]
    index = alphabet.index(letter)
    letter = reflector_mapping[index]
    print(f"Reflector Encryption: {letter}")

    # Reverse process through rotors

    # Rotor 3 reverse
    rotor3_inverse_mapping = ''.join(alphabet[rotor3_mapping.index(a)] for a in alphabet)
    index = (alphabet.index(letter) - rotor_positions[2]) % 26
    letter = rotor3_inverse_mapping[index]
    print(f"Wheel 1 Reverse Encryption: {letter}")

    # Rotor 2 reverse
    rotor2_inverse_mapping = ''.join(alphabet[rotor2_mapping.index(a)] for a in alphabet)
    index = (alphabet.index(letter) - rotor_positions[1]) % 26
    letter = rotor2_inverse_mapping[index]
    print(f"Wheel 2 Reverse Encryption: {letter}")

    # Rotor 1 reverse
    rotor1_inverse_mapping = ''.join(alphabet[rotor1_mapping.index(a)] for a in alphabet)
    index = (alphabet.index(letter) - rotor_positions[0]) % 26
    letter = rotor1_inverse_mapping[index]
    print(f"Wheel 3 Reverse Encryption: {letter}")

    # Step 4: Final plugboard encryption
    final_output = plugboard.transform_character(letter)
    print(f"Plugboard Encryption: {final_output}")
    print(f"Output (Lampboard): {final_output}")
    print("-----------------------------")

    # Step 5: Advance the rotors after each letter
    advance_rotors(rotor_positions, rotor_notches)

    return final_output


def encode_message_with_rotor_advance(plugboard, selected_rotors, selected_reflector, message, rotor_positions, rotor_notches_dict, ring_settings):
    """
    Encodes the entire message with rotor advancement for each letter.

    Args:
        plugboard (Plugboard): The plugboard instance for character transformations.
        selected_rotors (list): The list of selected rotors with their mappings.
        selected_reflector (tuple): The selected reflector's name and mapping.
        message (str): The message to be encoded.
        rotor_positions (list): The current positions of the rotors.
        rotor_notches_dict (dict): A dictionary mapping rotor names to their notch positions.
        ring_settings (list): The ring settings for the rotors.

    Returns:
        str: The encoded message after processing each letter.
    """
    # Validate rotor notches before processing
    for rotor in selected_rotors:
        rotor_name = rotor[0]  # Assuming rotor[0] contains the rotor name
        if rotor_name not in rotor_notches_dict:
            raise KeyError(f"{rotor_name} not found in rotor notches dictionary.")

    # Create rotor notches based on selected rotors
    try:
        rotor_notches = [rotor_notches_dict[rotor[0]] for rotor in selected_rotors]
    except KeyError as e:
        print(f"KeyError: {e} - This rotor is not in the rotor notches dictionary.")
        return None
    except TypeError as e:
        print(f"TypeError: {e} - Check the type of rotor_notches_dict and ensure it's a dictionary.")
        return None

    # Create rotor notches based on selected rotors
    #rotor_notches = [rotor_notches_dict[rotor[0]] for rotor in selected_rotors]

    encoded_message = []
    for letter in message:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # encode letter with current rotor positions
            encoded_letter = encode_letter_with_rotor_advance(
                plugboard,
                selected_rotors,
                selected_reflector,
                letter,
                rotor_positions,
                rotor_notches
            )

            encoded_message.append(encoded_letter)
            # Update rotor positions
            rotor_positions = update_rotor_positions(rotor_positions, rotor_notches_dict, selected_rotors)

        else:
            encoded_message.append(letter)  # Keep spaces or non-alphabetic characters as-is
    return ''.join(encoded_message)

