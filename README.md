# 🖥️ WF Console

## Introduction

**WF Console** is a Python utility designed to enhance terminal-based applications with ANSI-styled output and interactive menu systems. It supports clear and styled text rendering, user prompts, validated menu selections, and paginated DataFrame printing. It's ideal for CLI tools needing a richer, user-friendly interface.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## Installation

To use `WF Console`, run the following command.

```bash
pip install git+https://github.com/westonforbes/wf_console.git
```

---

## Usage

Here's a quick example of how to use the console:

```python
from wf_console import Console

# Simple styled print
Console.fancy_print("<GOOD>Success!</GOOD> <INFO>Info message here</INFO>")

# Show a simple menu
selection = Console.menu("Main Menu", ["Option A", "Option B"])

# Menu with input validation
index, value = Console.integer_only_menu_with_validation("Choose Option", ["Alpha", "Beta"])

# Paginated DataFrame display
import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
Console.paginated_print(df)
```

---

## Features

- 🎨 **ANSI Styling**: Use predefined tags like `<GOOD>`, `<BAD>`, `<INFO>`, etc., for colorful output.
- 📋 **Menu Systems**:
  - Basic menu with customizable title, prompt, prepend/append text.
  - Validated menu that ensures numeric input and range validation.
- 📊 **Paginated DataFrame Display**: View large data frames in the terminal with pagination.
- 🚀 **Cross-Platform Clear Screen Support**
- 🔁 **Reusable Tag Map via `Constants` Module**

---

## Dependencies

- Python 3.6+
- `pandas` (for `paginated_print`)

---

## Configuration

The `Constants` class contains ANSI escape codes used by the `Console` class. Tags are dynamically mapped from `Constants` and can be extended:

```python
class Constants:
    GOOD = "\033[32m"
    BAD = "\033[31m"
    RESET = "\033[0m"
    ...
```

Add new styles by inserting additional uppercase attributes into `Constants`.

---

## Documentation

### `Console.fancy_print(text: str)`
Parses tags like `<TAG>` and `</TAG>` and replaces them with matching ANSI codes for styled terminal output.

### `Console.fancy_input(text: str) -> str`
Styled prompt for user input.

### `Console.menu(title, item_list, input_message, prepend_str, append_str) -> str`
Creates a menu and returns raw user input (no validation).

### `Console.integer_only_menu_with_validation(...) -> tuple[int, str]`
Same as `menu()` but includes input validation for integer ranges.

### `Console.paginated_print(df: pd.DataFrame, page_size: int)`
Prints a DataFrame page-by-page, pausing for user input.

### `Console.press_enter_pause()`
Prompts user to press ENTER before continuing.

---

## Examples

```python
Console.fancy_print("<WARNING>This is a warning message</WARNING>")
index, selected = Console.integer_only_menu_with_validation(
    "Select Fruit", ["Apple", "Banana", "Cherry"]
)
```
