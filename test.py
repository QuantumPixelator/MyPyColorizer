#!/usr/bin/env python3
"""
Test script for MyPyColorizer
Demonstrates various color and style combinations
"""

from colorizer import Color

def test_basic_colors():
    """Test basic foreground colors"""
    print("=== Basic Colors ===")
    colors = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
    for color_name in colors:
        color_code = getattr(Color, color_name)
        print(Color.colorize(color_name.lower(), f"This is {color_name.lower()} text"))

def test_bright_colors():
    """Test bright colors"""
    print("\n=== Bright Colors ===")
    bright_colors = ['BRIGHT_RED', 'BRIGHT_GREEN', 'BRIGHT_YELLOW', 'BRIGHT_BLUE', 'BRIGHT_MAGENTA', 'BRIGHT_CYAN', 'BRIGHT_WHITE']
    for color_name in bright_colors:
        print(Color.colorize(color_name.lower(), f"This is {color_name.lower().replace('_', ' ')} text"))


def test_color_and_background_combinations():
    """Test foreground color on different background colors"""
    print("\n=== Foreground and Background Combinations ===")

    color = Color()
    # White text on Red background
    print(f"{color.WHITE}{color.RED_BG}White text on RED background{color.RESET}")

    # Black text on Cyan background
    print(f"{color.BLACK}{color.CYAN_BG}Black text on CYAN background{color.RESET}")

    # Yellow text on Blue background with BOLD style
    print(f"{color.BOLD_BRIGHT}{color.YELLOW}{color.BLUE_BG}Bold Yellow text on BLUE background{color.RESET}")

    # Bright White text on Black background
    print(f"{color.BRIGHT_WHITE}{color.BLACK_BG}Bright White text on BLACK background{color.RESET}")
    print("Hi")


def test_complex_styles():
    """Test complex combinations of styles"""
    print("\n=== Complex Style Combinations ===")

    color = Color()
    # Bold + Underline + Blue text
    print(f"{color.BOLD_BRIGHT}{color.UNDERLINE}{color.BLUE}Bold and Underlined Blue Text{color.RESET}")

    # Dim + Italic + Yellow text
    print(f"{color.DIM}{color.ITALIC}{color.YELLOW}Dim and Italic Yellow Text{color.RESET}")

    # Reverse + Magenta text
    print(f"{color.REVERSE}{color.MAGENTA}Reversed Magenta Text{color.RESET}")

    # Strikethrough + Bright Red text
    # Note: Strikethrough may not be supported in all terminals.
    print(f"{color.STRIKETHROUGH}{color.BRIGHT_RED}Strikethrough Bright Red Text{color.RESET}")
    print("Hi")



def test_styles():
    """Test text styles"""
    print("\n=== Text Styles ===")
    styles = ['BOLD_BRIGHT', 'DIM', 'ITALIC', 'UNDERLINE', 'BLINK', 'REVERSE']
    for style_name in styles:
        style_code = getattr(Color, style_name)
        print(f"{style_code}This is {style_name.lower().replace('_', ' ')} text{Color.RESET}")

def test_combined():
    """Test combining colors and styles"""
    print("\n=== Combined Styles ===")
    color = Color()
    print(f"{color.ITALIC}{color.BRIGHT_BLUE}This is italic bright blue{Color.RESET}")
    print(f"{color.UNDERLINE}{color.BRIGHT_GREEN}This is underlined bright green{Color.RESET}")
    print(f"{color.BOLD_BRIGHT}{color.MAGENTA}This is bold bright magenta{Color.RESET}")

def test_background():
    """Test background colors"""
    print("\n=== Background Colors ===")
    bg_colors = ['RED_BG', 'GREEN_BG', 'BLUE_BG', 'YELLOW_BG']
    for bg_name in bg_colors:
        bg_code = getattr(Color, bg_name)
        print(f"{bg_code}This has {bg_name.lower().replace('_bg', ' background')}{Color.RESET}")

if __name__ == "__main__":
    print("MyPyColorizer Test Suite")
    print("========================")

    test_basic_colors()
    test_bright_colors()
    test_styles()
    test_combined()
    test_background()
    test_complex_styles()
    test_color_and_background_combinations()


    print("\n=== Test Complete ===")
    print("Note: Colors may not display correctly in all terminals.")
    print("Test with different terminals for best results.")