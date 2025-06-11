import os
import re
from constants import *

class Console():


    def __init__(self):
        """
        Initializes the tag mapping dictionary by collecting all class-level constants 
        (attributes with uppercase names and string values). These are assumed to be 
        ANSI escape code tags used for styling terminal output.

        Attributes:
            TAG_MAP (Dict[str, str]): Mapping of tag names (e.g., 'RED') to ANSI codes.
        """      
        # Initialize an empty dictionary to store tag mappings.
        tag_map = {}

        # Loop through all attributes defined in the class (not instance).
        for key, value in self.__class__.__dict__.items():
            
            # Only include constants:
            # - Attribute name must be all uppercase (like 'RED', 'BOLD', etc.).
            # - Attribute value must be a string (we're targeting ANSI escape codes).
            if key.isupper() and isinstance(value, str):
                tag_map[key] = value  # Add to the tag map.

        # Assign the resulting dictionary to the instance variable.
        self.TAG_MAP = tag_map


    def clear(self) -> None:
        """
        Clears the terminal screen using an OS-specific command.
        Works on both Windows and Unix-like systems.
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    def fancy_print(self, text: str) -> None:
        """
        Prints the given text to the terminal, replacing tags like <TAG> and </TAG> 
        with corresponding ANSI escape codes defined in TAG_MAP.

        Parameters:
            text (str): The input string containing formatting tags to be styled and printed.
        """
        def replacer(match: re.Match) -> str:
            closing, tag = match.group(1), match.group(2)
            if closing:
                return self.RESET
            return self.TAG_MAP.get(tag, "")

        pattern = re.compile(r'<(/?)(\w+)>')
        styled_text = pattern.sub(replacer, text)
        print(styled_text + self.RESET)


    def fancy_input(self, text: str) -> str:
        """
        Displays styled input prompt by replacing formatting tags with ANSI codes,
        and returns the raw input from the user.

        Parameters:
            text (str): The prompt string containing <TAG> and </TAG> formatting tags.

        Returns:
            str: The user's raw input.
        """
        def replacer(match: re.Match) -> str:
            closing, tag = match.group(1), match.group(2)
            if closing:
                return self.RESET
            return self.TAG_MAP.get(tag, "")

        pattern = re.compile(r'<(/?)(\w+)>')
        styled_text = pattern.sub(replacer, text)
        return input(styled_text + self.RESET)


    def menu(self, title: str, item_list: list[str], input_message: str ='enter selection: ',  prepend_str: str = None, append_str: str = None) -> str:
        """
        Creates a simple menu and returns the user's selection (input is not validated).
        
        Parameters:
            title (str): Title to be displayed on the menu.
            item_list (list[str]): Items to display in the menu.
            input_message (str): Prompt message for user input (default is 'enter selection: ').

        Returns:
            str: Raw input entered by the user.
        """

        # First clear the console.
        self.clear()

        # Print the menu title.
        self.fancy_print(f"\n<MENU_TITLE>---{title}---</MENU_TITLE>")

        # Check that item_list is a list of strings.
        if not (isinstance(item_list, list) and all(isinstance(item, str) for item in item_list)): raise ValueError('item_list is not a list of strings.')

        
        if prepend_str is not None:
            # If prepend_str is provided, print it.
            self.fancy_print(prepend_str)
        
        self.fancy_print("")

        # Iterator.
        i = 1

        # For each item in list...
        for item in item_list:

            # Print out the menu option.
            self.fancy_print(f"<MENU_KEY>[{i:02}]</MENU_KEY> - <MENU_ITEM>{item}</MENU_ITEM>")

            # Increment the iterator.
            i += 1
        
        if append_str is not None:
            # If append_str is provided, print it.
            self.fancy_print(append_str)

        # Get the users selection.
        return self.fancy_input(f"\n<MENU_SELECTION_PROMPT>{input_message}</MENU_SELECTION_PROMPT>")


    def integer_only_menu_with_validation(self, title: str, item_list: list[str], input_message: str ='enter selection: ', prepend_str: str = None, append_str: str = None) -> tuple[int, str]:

        # Loop until we get a valid input.
        while True:

            # Call the menu function which renders the menu and input message without validating the input.
            selection = self.menu(title, item_list, input_message, prepend_str, append_str)

            # Try protect...
            try:

                # Convert the input to a integer.
                value = int(selection)

                # If the input converted sucessfully (implied by reaching this point) and the value is within range of the menu...
                if 0 < value <= len(item_list):

                    # Return the integer value of selection.
                    return value, item_list[value - 1]
                
                # If the input is a valid integer but is out of range...
                else:
                    self.fancy_print("<BAD>\nyour input is out of the menu range.</BAD>")
                    self.press_enter_pause()
            
            # If the input is not a integer...
            except ValueError:
                self.fancy_print("<BAD>\nyour input is non-numeric.</BAD>")
                self.press_enter_pause()


    def press_enter_pause(self):
        """
        Pauses the program until the user presses Enter.
        """
        self.fancy_input("<INPUT_PROMPT>press <KEYBOARD_KEY>ENTER</KEYBOARD_KEY><INPUT_PROMPT> to continue... </INPUT_PROMPT>")
        
if __name__ == "__main__":
    pass