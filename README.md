#  GET INVOLVED: Check out the pinned issues. Good for beginners.

# MyPyColorizer

A very simple way to add color to your Python CLI apps.

## Features

- Easy-to-use color class with ANSI escape codes
- Support for foreground and background colors
- Text styling (bold, italic, underline, etc.)
- Simple `colorize()` method for quick coloring
- Lightweight and dependency-free

## Installation

```bash
pip install mypycolorizer
```

## Usage

### Basic Usage

```python
from mypycolorizer.colorizer import Color

# Using the colorize method
print(Color.colorize("red", "Hello, World!"))

# Direct ANSI codes
print(f"{Color.GREEN}This is green text.{Color.RESET}")

# Combining styles
color = Color()
print(f"{color.ITALIC}{color.BRIGHT_BLUE}Styled text.{color.RESET}")

# Flexible color names using colorize()
print(Color.colorize("bright yellow", "This also works!"))

# Combining multiple styles with colorize()
styled = Color.colorize("bold bright", Color.colorize("underline", Color.colorize("blue", "Bold and Underlined Blue Text")))
print(styled)
```

### Available Colors

*** The colors can be upper/lowercase, or a combination. The app also handles spaces and dashes in the color name ***

**Foreground Colors:**

- BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
- BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE

**Background Colors:**
- BLACK_BG, RED_BG, GREEN_BG, YELLOW_BG, BLUE_BG, MAGENTA_BG, CYAN_BG, WHITE_BG

**Text Styles:**
- BOLD_BRIGHT, DIM, ITALIC, UNDERLINE, BLINK, RAPID_BLINK, REVERSE, HIDE, STRIKETHROUGH

## Contributing

This project welcomes contributions from developers of all skill levels, especially beginners!

### Ways to Contribute

- **Bug fixes**: Found an issue? Fix it!
- **New features**: Add more colors, styles, or functionality
- **Documentation**: Improve examples, comments, or this README
- **Testing**: Add test cases or verify compatibility
- **Code improvements**: Refactor, optimize, or clean up code

### Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/mypycolorizer.git`
3. Create a branch: `git checkout -b your-feature-name`
4. Make your changes
5. Test thoroughly
6. Commit: `git commit -m 'Add your feature'`
7. Push: `git push origin your-feature-name`
8. Open a Pull Request

### Guidelines

- Keep the code simple and lightweight
- Maintain backward compatibility
- Test with different terminals
- Follow Python best practices
- Add comments for new features

## Caveats

Not all escape codes work with all terminals. Be sure to test your terminal with the styles you would like to use.

## Project Structure

```
mypycolorizer/
├── colorizer.py    # Main color class
├── README.md      # This documentation
├── CONTRIBUTING.md # Contribution guidelines
└── LICENSE        # MIT License
```

## License

[MIT License](LICENSE)


## Acknowledgments

- Created to simplify terminal coloring in Python
- Inspired by other color libraries but designed for simplicity
