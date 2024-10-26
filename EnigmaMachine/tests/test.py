import unittest

from EnigmaMachine.core.enigmaPlugs import *
from EnigmaMachine.core.enigmaRotors import *


class TestEnigmaMachine(unittest.TestCase):
    def test_PlugLead(self):
        print("Running tests for PlugLead...")
        lead = PlugLead("AG")
        self.assertEqual(lead.encode("A"), "G")
        self.assertEqual(lead.encode("G"), "A")
        self.assertEqual(lead.encode("D"), "D")

        lead = PlugLead("DA")
        self.assertEqual(lead.encode("D"), "A")
        self.assertEqual(lead.encode("A"), "D")
        self.assertEqual(lead.encode("C"), "C")
        print("All tests for PlugLead passed!")

    def test_plugboard(self):
        print("Running plugboard tests...")
        test_cases = {
            'A': 'G',
            'G': 'A',
            'B': 'B',
            'C': 'C',
            'D': 'D',
            'E': 'E',
            'F': 'F',
        }
        plugboard = PlugLead("AG")
        for char, expected in test_cases.items():
            encoded = plugboard.encode(char)
            self.assertEqual(encoded, expected, f"Expected '{expected}', but got '{encoded}' for '{char}'")
            print(f"Encoded '{char}' -> '{encoded}'")
        print("Plugboard tests completed successfully.")


if __name__ == '__main__':
    unittest.main()