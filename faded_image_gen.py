# Written by Jacob Clouse 
# Edited on Windows 10 - may need to be edited if you want to use on Linux/MacOS

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import datetime
from PIL import Image, ImageDraw
import sys


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# --- Function to print out my Logo ---
def myLogo():
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("PICTURE BLENDER PYTHON SCRIPT")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("Created and Tested by: ")
    print("   __                  _         ___ _                       ")
    print("   \ \  __ _  ___ ___ | |__     / __\ | ___  _   _ ___  ___  ")
    print("    \ \/ _` |/ __/ _ \| '_ \   / /  | |/ _ \| | | / __|/ _ \ ")
    print(" /\_/ / (_| | (_| (_) | |_) | / /___| | (_) | |_| \__ \  __/ ")
    print(" \___/ \__,_|\___\___/|_.__/  \____/|_|\___/ \__,_|___/\___| ")
    print("Dedicated to Peter Zlomek & Harely Alderson III")
    print("\n")


# --- Function to Defang date time ---
def defang_datetime():
    current_datetime = f"_{datetime.datetime.now()}"

    current_datetime = current_datetime.replace(":", "_")
    current_datetime = current_datetime.replace(".", "-")
    current_datetime = current_datetime.replace(" ", "_")

    return current_datetime


# --- Function to import the Command line arguments - for dominant and recessive images
# https://cs.stanford.edu/people/nick/py/python-main.html=
def returnPics():
    incomingDominant = sys.argv[1]
    incomingRecessive = sys.argv[2]
    return incomingDominant, incomingRecessive


# --- Function to Mix Images ---
def fade_images(dominant_image, recessive_image, output_path, fade_ratio):
    # Open the two images
    dominant_img = Image.open(dominant_image)
    recessive_img = Image.open(recessive_image)

    # Resize the images to have the same dimensions
    dominant_img = dominant_img.resize(recessive_img.size)

    # Create a new image with the same dimensions
    blended_image = Image.new("RGB", dominant_img.size)

    # Create an ImageDraw object to draw on the blended image
    draw = ImageDraw.Draw(blended_image)

    # Iterate over each pixel and blend the two images
    for x in range(dominant_img.width):
        for y in range(dominant_img.height):
            # Get the RGB values of each pixel from both images
            dominant_pixel = dominant_img.getpixel((x, y))
            recessive_pixel = recessive_img.getpixel((x, y))

            # Calculate the blended pixel value
            blended_pixel = tuple(
                int(dominant_pixel[i] * fade_ratio + recessive_pixel[i] * (1 - fade_ratio))
                for i in range(3)
            )

            # Draw the blended pixel on the new image
            draw.point((x, y), blended_pixel)

    # Save the blended image to the output path
    blended_image.save(output_path)
    print("Blended image saved to:", output_path)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Main
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
myLogo()
current_Date_time = defang_datetime()  # Get Datetime
dominant_image_path, recessive_image_path = returnPics()
# dominant_image_path = "dsa.jpg"
# recessive_image_path = "dan.jpg"
fade_ratio = 0.7  # Adjust this value to control the fading effect (0.0 - 1.0)
output_image_path = f"blended_image_@{str(fade_ratio)}ratio_{current_Date_time}.jpg"


fade_images(dominant_image_path, recessive_image_path, output_image_path, fade_ratio)
