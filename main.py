import fontforge
import os

# Create a new font
font = fontforge.font()

# Set font properties
font.familyname = "MyCustomFont"
font.fontname = "MyCustomFont"
font.fullname = "My Custom Font"

# Define the folder containing your PNG images
image_folder = "path/to/your/images/"

# Define the characters you want to include in your font
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Define the baseline and width for your characters
baseline = 0
width = 500

# Iterate through uppercase letters and add them to the font
for index, letter in enumerate(uppercase_letters):
    # Create a new glyph with the Unicode codepoint
    glyph = font.createChar(ord(letter))

    # Load the corresponding image file
    image_path = os.path.join(image_folder, f"{letter}.png")
    glyph.importOutlines(image_path)

    # Set glyph properties
    glyph.width = width
    glyph.vwidth = width
    glyph.align("baseline", baseline)

# Generate the TTF file
font.generate("MyCustomFont.ttf")
