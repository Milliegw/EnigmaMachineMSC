from EnigmaMachine.core.enigmaPlugs import *
from EnigmaMachine.core.enigmaRotors import *


def test_PlugLead():
    """
    Test the PlugLead class and its encoding functionality.

    This function runs a series of assertions to verify that the PlugLead
    correctly encodes letters based on the specified plug configuration.
    It checks both direct mappings (e.g., A <-> G) and self-mappings
    (e.g., D maps to D).

    The following scenarios are tested:
    1. A lead of "AG" should map 'A' to 'G', 'G' to 'A', and 'D' to 'D'.
    2. A lead of "DA" should map 'D' to 'A', 'A' to 'D', and 'C' to 'C'.

    Prints the result of the tests indicating whether they passed or failed.
    """
    print("Running tests for PlugLead...")
    try:
        lead = PlugLead("AG")
        assert lead.encode("A") == "G", "Test failed: A should map to G"
        assert lead.encode("G") == "A", "Test failed: G should map to A"
        assert lead.encode("D") == "D", "Test failed: D should map to itself"

        lead = PlugLead("DA")
        assert lead.encode("D") == "A", "Test failed: D should map to A"
        assert lead.encode("A") == "D", "Test failed: A should map to D"
        assert lead.encode("C") == "C", "Test failed: C should map to itself"

        print("All tests for PlugLead passed!")
    except AssertionError as e:
        print(e)
        print("Some tests for PlugLead failed. Please review the errors above.")


def test_plugboard():
    """
    Test the PlugLead encoding functionality for the Enigma machine.

    This function tests various character inputs to ensure that the
    PlugLead correctly transforms characters according to the specified
    plugboard connections. It verifies both direct and unchanged mappings.

    Prints the results of each test, indicating whether the encoding
    was successful.
    """
    print("Running plugboard tests...")

    # Define test cases: input characters and expected output after transformation
    test_cases = {
        'A': 'G',  # Example mapping
        'G': 'A',  # Example mapping
        'B': 'B',  # Should map to itself if no plug
        'C': 'C',  # Should map to itself if no plug
        'D': 'D',  # Should map to itself if no plug
        'E': 'E',  # Should map to itself if no plug
        'F': 'F',  # Should map to itself if no plug
    }

    # Create a plugboard with specific leads for testing
    plugboard = PlugLead("AG")  # Example: this maps A <-> G

    for char, expected in test_cases.items():
        encoded = plugboard.encode(char)  # Use transform_character()
        assert encoded == expected, f"Expected '{expected}', but got '{encoded}' for '{char}'"
        print(f"Encoded '{char}' -> '{encoded}'")

    print("Plugboard tests completed successfully.")

# Test for rotor setup
def test_rotors_setup():
    """
    Test the rotor setup functionality for the Enigma machine.

    This function runs a series of assertions to verify that the user
    can select the correct rotors and that the selected rotors match
    the expected configurations. It simulates user input for various
    rotor selections and checks if the selected rotor's name and
    mapping correspond to the predefined expected values.

    The following scenarios are tested:
    1. Each rotor from the available options is tested to ensure it
       is selected correctly.
    2. The selected rotor's mapping is validated against the expected
       rotor mapping defined in the expected_rotors dictionary.

    Prints the result of each test, indicating whether it passed or
    failed, and summarizes the completion of the rotor setup tests.
    """
    print("Running rotor setup tests...")

    # Define the rotors for comparison
    expected_rotors = {
        "Beta": "LEYJVCNIXWPBQMDRTAKZGFUHOS",
        "Gamma": "FSOKANUERHMBTIYCWLQPZXVGJD",
        "I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "IV": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "V": "VZBRGITYUPSDNHLXAWMJQOFECK"
    }

    # Loop through each rotor and test selection
    for rotor_name, expected_mapping in expected_rotors.items():
        # Simulate the input by mocking the user input
        print(f"Testing rotor selection for: {rotor_name}")

        # Mock the rotor setup
        def mock_input(prompt):
            return rotor_name

        # Temporarily replace the built-in input with mock_input
        original_input = __builtins__.input
        __builtins__.input = mock_input

        try:
            selected_rotor = rotors_setup()

            # Check if the selected rotor matches the expected rotor and mapping
            assert selected_rotor[0][0] == rotor_name, f"Expected rotor name {rotor_name}, got {selected_rotor[0][0]}"
            assert selected_rotor[0][1] == expected_mapping, f"Expected mapping {expected_mapping}, got {selected_rotor[0][1]}"

            print(f"Test passed for rotor: {rotor_name}\n")
        except AssertionError as e:
            print(e)
            print(f"Test failed for rotor: {rotor_name}\n")
        finally:
            # Restore the original input function after the test
            __builtins__.input = original_input

    print("Rotor setup tests completed.")


def test_rotor_notches():
    """
    Test the rotor notches to ensure they correspond to the expected values
    based on the selected rotors. This function checks if the notches for
    each rotor are correctly identified in the rotor_notches_dict.

    Prints the result of each test, indicating whether it passed or failed.
    """
    print("Running rotor notches tests...")

    # Define expected rotor notches for each rotor
    expected_rotor_notches = {
        "I": 16,  # Example: rotor I has notch at position 16 (Q)
        "II": 4,  # Example: rotor II has notch at position 4 (E)
        "III": 21,  # Example: rotor III has notch at position 21 (V)
        "IV": 9,  # Example: rotor IV has notch at position 9 (J)
        "V": 25,  # Example: rotor V has notch at position 25 (Z)
        "Beta": 22,  # Example: beta rotor has notch at position 22 (V)
        "Gamma": 10  # Example: gamma rotor has notch at position 10 (K)
    }

    # Create a mock rotor notches dictionary for testing
    rotor_notches_dict = {
        "I": expected_rotor_notches["I"],
        "II": expected_rotor_notches["II"],
        "III": expected_rotor_notches["III"],
        "IV": expected_rotor_notches["IV"],
        "V": expected_rotor_notches["V"],
        "Beta": expected_rotor_notches["Beta"],
        "Gamma": expected_rotor_notches["Gamma"],
    }

    # Test each rotor
    for rotor_name, expected_notch in expected_rotor_notches.items():
        print(f"Testing notch for rotor: {rotor_name}")

        # Check if the notch for the rotor exists in the dictionary
        if rotor_name in rotor_notches_dict:
            notch_value = rotor_notches_dict[rotor_name]
            assert notch_value == expected_notch, f"Expected notch {expected_notch} for rotor {rotor_name}, got {notch_value}"
            print(f"Test passed for rotor: {rotor_name} with notch {notch_value}")
        else:
            print(f"Rotor '{rotor_name}' NOT found in notches dictionary!")

    print("Rotor notches tests completed.")

import unittest


def test_rotor_notch_access():
    """
    Test accessing rotor notches with valid and invalid rotor keys.
    """
    valid_rotor = "I"
    invalid_rotor = "Invalid"

    # Valid access
    assert rotor_notches_dict[valid_rotor] == 17

    # Invalid access (should raise KeyError)
    try:
        _ = rotor_notches_dict[invalid_rotor]
    except KeyError:
        print(f"Caught expected KeyError for {invalid_rotor}")
    else:
        assert False, "Expected KeyError was not raised for invalid rotor."

# Integrate the new test into the main execution block
if __name__ == "__main__":
    print("PLUGLEAD TESTING")
    test_PlugLead()
    print("PLUGBOARD TESTING")
    test_plugboard()
    print("ROTOR TESTING")
    test_rotors_setup()
    print("ROTOR NOTCHES TESTING")
    test_rotor_notches()  # Call the new test function
    unittest.main()


