"""
WF Console - A utility class for enhanced terminal output with ANSI styling and menu creation.
"""
import os
import re
import sys
import pandas as pd
from .constants import Constants

class Console():

    # Class-level tag map initialization
    TAG_MAP = {}
    
    # Initialize the tag map at class level
    for key, value in Constants.__dict__.items():
        if key.isupper() and isinstance(value, str):
            TAG_MAP[key] = value

    @staticmethod
    def clear() -> None:
        """
        Clears the terminal screen using an OS-specific command.
        Works on both Windows and Unix-like systems.
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    @staticmethod
    def clear_last_line():
        """
        Clear the last line in the console.
        """
        
        # Move cursor up.
        sys.stdout.write('\x1b[1A')
        
        # Clear entire line.
        sys.stdout.write('\x1b[2K')
        sys.stdout.flush()

    @staticmethod
    def fancy_print(text: str) -> None:
        """
        Prints the given text to the terminal, replacing tags like <TAG> and </TAG> 
        with corresponding ANSI escape codes defined in TAG_MAP.

        Parameters:
            text (str): The input string containing formatting tags to be styled and printed.
        """
        def replacer(match: re.Match) -> str:
            closing, tag = match.group(1), match.group(2)
            if closing:
                return Constants.RESET
            return Console.TAG_MAP.get(tag, "")

        pattern = re.compile(r'<(/?)(\w+)>')
        styled_text = pattern.sub(replacer, text)
        print(styled_text + Constants.RESET)

    @staticmethod
    def fancy_input(text: str) -> str:
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
                return Constants.RESET
            return Console.TAG_MAP.get(tag, "")

        pattern = re.compile(r'<(/?)(\w+)>')
        styled_text = pattern.sub(replacer, text)
        return input(styled_text + Constants.RESET)

    @staticmethod
    def menu(title: str, item_list: list[str], input_message: str ='enter selection: ',  prepend_str: str = None, append_str: str = None) -> str:
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
        Console.clear()

        # Print the menu title.
        Console.fancy_print(f"\n---{title}---")

        # Check that item_list is a list of strings.
        if not (isinstance(item_list, list) and all(isinstance(item, str) for item in item_list)): raise ValueError('item_list is not a list of strings.')

        
        if prepend_str is not None:
            # If prepend_str is provided, print it.
            Console.fancy_print(prepend_str)
        
        Console.fancy_print("")

        # Iterator.
        i = 1

        # For each item in list...
        for item in item_list:

            # Print out the menu option.
            Console.fancy_print(f"<MENU_KEY>[{i:02}]</MENU_KEY> - <MENU_ITEM>{item}</MENU_ITEM>")

            # Increment the iterator.
            i += 1
        
        if append_str is not None:
            # If append_str is provided, print it.
            Console.fancy_print(append_str)

        # Get the users selection.
        return Console.fancy_input(f"\n<MENU_SELECTION_PROMPT>{input_message}</MENU_SELECTION_PROMPT>")

    @staticmethod
    def integer_only_menu_with_validation(title: str, item_list: list[str], input_message: str ='enter selection: ', prepend_str: str = None, append_str: str = None) -> tuple[int, str]:

        # Loop until we get a valid input.
        while True:

            # Call the menu function which renders the menu and input message without validating the input.
            selection = Console.menu(title, item_list, input_message, prepend_str, append_str)

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
                    Console.fancy_print("<BAD>\nyour input is out of the menu range.</BAD>")
                    Console.press_enter_pause()
            
            # If the input is not a integer...
            except ValueError:
                Console.fancy_print("<BAD>\nyour input is non-numeric.</BAD>")
                Console.press_enter_pause()

    @staticmethod
    def paginated_print(df: pd.DataFrame, page_size: int = 10):
        """
        Pretty prints a DataFrame in chunks, with row numbers, prompting the user to press Enter to continue.

        Args:
            df (pd.DataFrame): The DataFrame to print.
            page_size (int): Number of rows to display per page.
        """
        total_rows = len(df)
        pages = (total_rows + page_size - 1) // page_size  # Ceiling division
        row_num_width = len(str(total_rows - 1))  # Zero-padding width

        for page in range(pages):
            start = page * page_size
            end = start + page_size
            chunk = df.iloc[start:end].copy()

            # Create a row number column with zero-padded values
            row_numbers = [str(i).zfill(row_num_width) for i in range(start, min(end, total_rows))]
            chunk.insert(0, 'Row', row_numbers)

            Console.clear()
            Console.fancy_print(f"<DATA>Displaying rows {start+1} to {min(end, total_rows)} of {total_rows}\n</DATA>")
            Console.fancy_print(f"<DATA>{chunk.to_string(index=False)}</DATA>")

            if end < total_rows:
                result = Console.fancy_input(f"<INPUT_PROMPT>type <KEYBOARD_KEY>n</KEYBOARD_KEY><INPUT_PROMPT> to quit or press </INPUT_PROMPT><KEYBOARD_KEY>ENTER</KEYBOARD_KEY><INPUT_PROMPT> to continue... </INPUT_PROMPT>")
                if result.strip().lower() == 'n':
                    break
            else:
                Console.press_enter_pause()

    @staticmethod
    def press_enter_pause():
        """
        Pauses the program until the user presses Enter.
        """
        Console.fancy_input("<INPUT_PROMPT>press <KEYBOARD_KEY>ENTER</KEYBOARD_KEY><INPUT_PROMPT> to continue... </INPUT_PROMPT>")
        