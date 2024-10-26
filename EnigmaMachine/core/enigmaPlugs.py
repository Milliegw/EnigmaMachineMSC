"""
enigmaPlugs.py
This module defines the PlugLead and Plugboard classes, which represent the
connections on the Enigma Machine's plugboard. It allows for character encoding
through plug leads and manages user input for plug lead configuration.
"""

# PlugLead Class
class PlugLead:

    """Represents a single plug lead that connects two letters in the plugboard."""
    def __init__(self, mapping):
        """Initializes a PlugLead with a pair of letters.

                Args:
                    mapping (str): A string of exactly two uppercase letters representing the connection.

                Raises:
                    ValueError: If the mapping does not consist of two letters.
        """
        # Each lead in the enigma machine connects two plugs in the plugboard
        if len(mapping) != 2 or not mapping.isalpha():
            raise ValueError("Mapping must be a pair of letters.")
        # Make the mapping uppercase
        self.mapping = mapping.upper()

    def encode(self, character):
        """Encodes the character by swapping it if connected to a plug lead.

                Args:
                    character (str): The character to encode.

                Returns:
                    str: The encoded character, or the original character if no connection exists.
        """
        # Encode the character by swapping it if it's connected to a plug lead
        character = character.upper()
        if character == self.mapping[0]:
            return self.mapping[1]
        elif character == self.mapping[1]:
            return self.mapping[0]
        return character

# Plugboard class
class Plugboard:
    """Represents the entire plugboard, storing multiple PlugLead objects to encode characters."""
    # uses them to encode characters
    def __init__(self):
        # Initialize an empty list to store plug leads (PlugLead objects)
        self.plug_leads = []

    def add_lead(self, plug_lead):
        """Adds a plug lead to the plug board.

                Args:
                    plug_lead (PlugLead): The PlugLead object to be added.
        """
        self.plug_leads.append(plug_lead)

    # This is the encode method but named something different to avoid
    # confusion with encode in PlugLead
    def transform_character(self, character):
        """Transforms the character through the plug leads.

        Args:
            character (str): The character to transform.

        Returns:
            str: The transformed character, or the original character if no change occurs.
        """
        for lead in self.plug_leads:
            new_char = lead.encode(character)  # 'encode' is from PlugLead
            if new_char != character:
                return new_char # If a change is made, return the new character
        return character  # Return the original character if no transformation is done

def get_user_leads():
    """Prompts the user for plugboard leads and creates a Plugboard object.

    Returns:
        Plugboard: The Plugboard object containing the user's plug leads.
    """
    plugboard = Plugboard()
    lead_count = 10  # There are 10 plug leads allowed
    used_characters = set()  # Track used characters
    all_leads = []

    for i in range(lead_count):
        while True:
            user_input = input(f"Please enter Lead {i + 1} (e.g., 'AB'): ").strip().upper()

            # Validate that the input is two unique letters, and neither has been used already
            if len(user_input) == 2 and user_input.isalpha() and user_input[0] not in used_characters and user_input[
                1] not in used_characters:
                plugboard.add_lead(PlugLead(user_input))
                used_characters.update(user_input)  # Mark both characters as used
                all_leads.append(user_input)
                break
            else:
                print("Invalid input. Please enter a pair of unique letters not already entered.")

    # After all 10 leads are entered, confirm and print them back in a box
    print("\nAll 10 leads have been entered successfully!\n")
    print("Here are your leads for today:")
    print_leads_in_box(all_leads)

    return plugboard

def print_leads_in_box(leads):
    """Prints the leads in a formatted box.

    Args:
        leads (list): The list of leads to be printed.
    """
    # Determine the box width dynamically based on the longest lead string length
    box_width = 20
    print("+" + "-" * (box_width - 2) + "+")
    for lead in leads:
        print(f"| Lead: {lead} " + " " * (box_width - len(lead) - 8) + "|")
    print("+" + "-" * (box_width - 2) + "+")

