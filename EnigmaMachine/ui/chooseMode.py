from EnigmaMachine.core.encodingMessage import encode_letter_with_rotor_advance

def encode_letter_with_steps(plugboard, selected_rotors, selected_reflector, letter, rotor_positions,
                             rotor_notches_dict, ring_settings):
    steps = []

    # Track keyboard input and rotor positions
    steps.append(f"Keyboard Input: {letter}")
    steps.append(f"Rotors Position: {rotor_positions}")

    # Encode the letter
    encoded_letter = encode_letter_with_rotor_advance(
        plugboard,
        selected_rotors,
        selected_reflector,
        letter,
        rotor_positions,
        rotor_notches_dict
    )

    steps.append(f"Output (Lampboard): {encoded_letter}")

    return encoded_letter, "\n".join(steps)

def encode_message_with_steps(plugboard, selected_rotors, selected_reflector, message, rotor_positions,
                              rotor_notches_dict, ring_settings):
    all_steps = []
    encoded_message = ""

    for letter in message:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            encoded_letter, steps = encode_letter_with_steps(
                plugboard,
                selected_rotors,
                selected_reflector,
                letter,
                rotor_positions,
                rotor_notches_dict,
                ring_settings
            )
            encoded_message += encoded_letter
            all_steps.append(steps)
        else:
            encoded_message += letter  # Handle non-alphabetic characters like spaces

    return encoded_message, "\n-----------------------------\n".join(all_steps)

def choose_mode_and_encode(plugboard, selected_rotors, selected_reflector, rotor_positions, rotor_notches_dict, ring_settings):
    mode = input("Would you like to enter the message letter by letter (L) or as a full phrase (P)? ").strip().upper()

    if mode == "L":
        input_phrase = ""
        encoded_message = ""

        while True:
            letter = input("Enter a letter to encode (or press Enter to finish): ").strip().upper()

            if letter == "":
                break  # Exit when the user finishes input

            if len(letter) != 1 or letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("Please enter a valid letter (A-Z).")
                continue

            # Encode the letter with steps
            encoded_letter, encryption_steps = encode_letter_with_steps(
                plugboard,
                selected_rotors,
                selected_reflector,
                letter,
                rotor_positions,
                rotor_notches_dict,
                ring_settings
            )

            print(f"\nEncryption Steps for '{letter}':\n{encryption_steps}")
            print(f"Encoded letter: {encoded_letter}")

            input_phrase += letter
            encoded_message += encoded_letter

        print(f"\nFinal input phrase: {input_phrase}")
        print(f"Final encoded message: {encoded_message}")

    elif mode == "P":
        input_message = input("Enter a message to encode (max 250 characters): ").strip().upper()

        encoded_message, all_steps = encode_message_with_steps(
            plugboard,
            selected_rotors,
            selected_reflector,
            input_message,
            rotor_positions,
            rotor_notches_dict,
            ring_settings
        )

        print(f"\nDetailed Encryption Steps:\n{all_steps}")
        print(f"\nFinal input phrase: {input_message}")
        print(f"Final encoded message: {encoded_message}")

    else:
        print("Invalid option. Please choose L for letter-by-letter or P for full phrase.")