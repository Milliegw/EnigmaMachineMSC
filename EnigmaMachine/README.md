**Enigma Machine Project**

This project simulates the workings of the Enigma Machine, a cipher device used by the Germans during World War II for secure communication. The Enigma Machine encrypts messages through a series of rotors and plugboards, making the encoding process complex and secure.

Table of Contents

	•	How the Enigma Machine Works
	•	Project Structure
	•	Classes and Functions
	•	Encoding Process
	•	Usage

**How the Enigma Machine Works**

The Enigma Machine uses a combination of rotors, a plugboard, and a reflector to encrypt messages.
Each letter is passed through a series of components, each modifying the letter based on its current settings. The machine’s complexity arises from the numerous possible configurations, which greatly enhances security.

Key Components:

	1.	Rotors: Each rotor contains a wiring configuration that shifts the input letter based on its position. The machine typically uses three rotors, which can be selected by the user.
	2.	Plugboard: Before a letter is processed by the rotors, it passes through a plugboard where pairs of letters are swapped.
	3.	Reflector: After passing through the rotors, the signal is reflected back through the rotors, effectively doubling the encryption.
	4.	Rotor Notches: These are specific positions on the rotors that trigger the movement of adjacent rotors, simulating a stepping mechanism.

**Project Structure**

The project is organized into several modules:

	•	main.py: The entry point of the application that manages the user interface and the overall encoding process.
	•	chooseMode.py: Contains functions to select modes of operation for the encoding process.
	•	encodingMessage.py: Handles the encoding logic, including rotor advancement and letter encryption.
	•	enigmaPlugs.py: Manages the plugboard settings.
	•	enigmaRotors.py: Contains the definitions and behaviors of the rotors.
	•	test.py: Contains unit tests for various functionalities.
	•	welcome.py: Displays a welcome message and user instructions.

**Classes and Functions**

Classes and Their Functions

Functions
    
main.py
	- typing_welcome_message(): Displays a welcome message.
	- get_user_leads(): Retrieves user input for the plugboard.
	- rotors_setup(): Allows users to select rotors.
	- reflectors_setup(): Allows users to select a reflector.
	- choose_mode_and_encode(...): Encodes the input based on selected components.
	
chooseMode.py
	- choose_mode_and_encode(...): Manages user input mode and encoding process.
	
encodingMessage.py
	- encode_letter_with_steps(...): Encodes a letter and tracks the steps.
	- advance_rotors(...): Advances the rotor positions based on their notches.

enigmaPlugs.py
	- Functions related to plugboard configurations.

enigmaRotors.py
	- Defines rotor settings, including configurations and notch positions.

**Main Module**

File: main.py

This module serves as the entry point of the application. It coordinates user interactions and orchestrates the main processes of setting up the Enigma Machine and encoding messages.

Key Functions:

	•	typing_welcome_message()
	•	Purpose: Displays a welcome message with a typing effect, enhancing the user experience.
	•	Usage: Called at the start of the program to greet the user.
	•	get_user_leads()
	•	Purpose: Retrieves plugboard lead settings from the user. This function prompts the user to input the connections between letters for the plugboard, ensuring unique uppercase letter pairs are provided.
	•	Returns: A Plugboard object with the user’s specified settings.
	•	rotors_setup()
	•	Purpose: Prompts the user to select rotors from a predefined list. The user chooses three rotors that will form the core of the encryption process.
	•	Returns: A list of selected rotors and their configurations.
	•	reflectors_setup()
	•	Purpose: Prompts the user to choose a reflector. The reflector is responsible for reflecting signals back through the rotors during encryption.
	•	Returns: The selected reflector and its wiring configuration.
	•	choose_mode_and_encode()
	•	Purpose: Orchestrates the entire process of selecting plugboard, rotors, and reflector, then encoding the user’s input message. Depending on the mode chosen, it handles phrase input or single-letter input.

***PLUGBOARD AND PLUGLEAD MODULE***

1.	PlugLead

Purpose: Represents a single plug lead that connects two letters in the plugboard.

Constructor:
	•	__init__(self, mapping: str): Initializes a PlugLead with a pair of letters. Raises a ValueError if the mapping does not consist of exactly two uppercase letters.

Methods:
	•	encode(self, character: str) -> str: Encodes the provided character by swapping it with its corresponding pair if connected. Returns the original character if no connection exists.

2. Plugboard

Purpose: Represents the entire plugboard, which stores multiple PlugLead objects to perform character encoding.

Constructor:
	•	__init__(self): Initializes an empty list to store plug leads.

Methods:
	•	add_lead(self, plug_lead: PlugLead): Adds a given PlugLead object to the plugboard.
	•	transform_character(self, character: str) -> str: Transforms the provided character by passing it through all plug leads. Returns the transformed character if any changes are made; otherwise, returns the original character.

Functions:

	•	get_user_leads() -> Plugboard: Prompts the user to input their plug leads. Validates the input to ensure only unique uppercase letter pairs are accepted. Returns a Plugboard object containing the user’s specified leads.
	•	print_leads_in_box(leads: list): Prints the entered plug leads in a formatted box, enhancing visibility for user confirmation.

Usage Example

To use the plugboard functionality, instantiate the Plugboard class, add PlugLead objects, and utilize the transform_character method to encode characters based on user-defined connections.

***Rotor Module***

enigmaRotors.py

This module manages the configuration and setup of rotors and reflectors in the Enigma Machine, which are crucial for the encryption process. Each rotor has a specific wiring configuration and a notch position, which determines when the next rotor should advance.

Key Components

Rotor Notches Dictionary

- rotor_notches_dict: A dictionary mapping each rotor to its notch position. This position indicates when the rotor will trigger the advancement of the adjacent rotor.

- Rotor	Notch Position
I	17
II	5
III	22
IV	9
V	25
Beta	15
Gamma	2

Functions:
	•	rotors_setup() -> list: Prompts the user to select three rotors for the machine. Validates user input and returns a list of selected rotors and their corresponding wiring configurations.
	•	reflectors_setup() -> tuple: Prompts the user to select a reflector. Validates the input and returns the selected reflector and its wiring.
	•	print_rotors_to_choose(rotors: dict): Prints the list of available rotors to the console, allowing the user to see their options.
	•	print_reflectors_to_choose(reflectors: dict): Prints the list of available reflectors to the console.
	•	ring_settings_setup(selected_rotors: list) -> list: This function is currently defined but not implemented. It will be used to handle the ring settings for the selected rotors, which will affect the rotor’s starting positions.


Usage Example

To set up the rotors and reflectors, call rotors_setup() and reflectors_setup(). The selected configurations will be used in the encoding process of the Enigma Machine.

**Choose Mode Module**

File: chooseMode.py

This module provides a mechanism for the user to select how they would like to interact with the Enigma Machine, particularly whether to input a full phrase at once or encode letters one by one.

Key Functions:

	•	choose_mode_and_encode(...)
	•	Purpose: Manages user input modes and controls the encoding process. Depending on the mode selected, the function handles the step-by-step encoding of letters or the encoding of a full phrase at once.
	•	Usage: Called during the setup process, it ensures that the encoding process fits the user’s chosen mode.

**Encoding Process Module**

File: encodingMessage.py

This module is central to the encoding process. It handles the encryption of letters and the advancement of rotors after each letter is encoded.

Key Functions:

	•	encode_letter_with_steps(...)
	•	Purpose: Encodes a single letter and provides detailed feedback on each step of the process (e.g., plugboard transformation, rotor encryption, reflector step, and reverse rotor encryption). This function is useful for understanding how each component of the Enigma Machine alters the input letter.
	•	Returns: The encoded letter, along with detailed information about the intermediate steps.
	•	advance_rotors(...)
	•	Purpose: Advances the rotors after each letter is encoded, simulating the stepping mechanism of the real Enigma Machine. If a rotor reaches its notch position, the adjacent rotor also advances.

**Welcome Module**

File: welcome.py

This module focuses on providing a polished introduction for the user when they launch the Enigma Machine simulator.

Key Functions:

	•	typing_welcome_message()
	•	Purpose: Displays a welcome message with a typing effect to engage the user as they start interacting with the program. The message can include a brief explanation of what the Enigma Machine is and how the program works.

**Test Module**

File: test.py

This module contains unit tests to verify that the components of the Enigma Machine (e.g., plugboard, rotors, and encoding process) function as expected.

Key Components:

	•	Tests for PlugLead and Plugboard: Ensure that the PlugLead class correctly swaps letters and that the Plugboard applies the correct transformations.
	•	Tests for Rotors and Rotor Advancement: Validate that rotors are configured correctly and that rotor advancement occurs as intended.
	•	Encoding Process Tests: Test the end-to-end encoding of messages to ensure that the components integrate correctly and provide the expected output.


**Encoding Process**

The encoding process occurs in several steps:

	1.	User Setup: The user is prompted to select the plugboard settings, rotors, and reflector.
	2.	Initial Positions: The rotors are set to their initial positions (usually all at zero).
	3.	Encoding Loop:
	•	The user inputs a letter.
	•	The letter first goes through the plugboard, where it may be swapped with another letter.
	•	It passes through the rotors, which modify its position based on their wiring and current settings.
	•	After reaching the reflector, the signal is sent back through the rotors in reverse order.
	•	Finally, it returns through the plugboard to produce the encrypted letter.
	4.	Rotor Advancement: After each letter is encoded, the rightmost rotor steps forward. If it reaches a notch, it causes the next rotor to advance, continuing the process.
	5.	Output: The encoded message is displayed to the user.

**Usage**

To run the project, execute main.py:
python main.py

Follow the prompts to configure the machine and input your message for encoding.