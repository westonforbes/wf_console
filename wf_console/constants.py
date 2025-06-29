class Constants:
    """
    This class contains ANSI escape codes for terminal text formatting.
    It includes styles for colors, backgrounds, and text attributes.
    """
    # Reset.---------------------------------------------------------------------------------------
    RESET = "\033[0m"

    # Regular colors.------------------------------------------------------------------------------
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright colors.-------------------------------------------------------------------------------
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Regular backgrounds.-------------------------------------------------------------------------
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Bright backgrounds.--------------------------------------------------------------------------
    BG_BRIGHT_BLACK = "\033[100m"
    BG_BRIGHT_RED = "\033[101m"
    BG_BRIGHT_GREEN = "\033[102m"
    BG_BRIGHT_YELLOW = "\033[103m"
    BG_BRIGHT_BLUE = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN = "\033[106m"
    BG_BRIGHT_WHITE = "\033[107m"

    # Tagged style modifiers.----------------------------------------------------------------------
    UNDERLINE = "\033[4m"
    GOOD = GREEN
    BAD = RED
    WARNING = YELLOW
    INFO = MAGENTA

    FUNCTION = BLUE + UNDERLINE
    CLASS = BLUE + UNDERLINE
    DATA = BRIGHT_CYAN


    # Menu style modifiers.------------------------------------------------------------------------
    MENU_TITLE = MAGENTA
    MENU_ITEM = YELLOW
    MENU_KEY = GREEN
    MENU_NAV_ITEM = CYAN
    MENU_SELECTION_PROMPT = CYAN

    KEYBOARD_KEY = MAGENTA + BG_GREEN
    OPTION = GREEN
    INPUT_PROMPT = CYAN