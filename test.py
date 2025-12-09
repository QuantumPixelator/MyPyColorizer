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

    print("\n=== Test Complete ===")
    print("Note: Colors may not display correctly in all terminals.")
    print("Test with different terminals for best results.")