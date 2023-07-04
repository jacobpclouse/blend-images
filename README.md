# blend-images
Image Fading Program

This program allows you to fade two images together, with one image being dominant and the other being recessive. It takes two input images, resizes them to the same dimensions, and creates a new image where the dominant image is prominent while the recessive image is visible but more faded. The fading effect is controlled by adjusting the fade ratio, which determines the amount of blending between the two images.

Features:
- Fades two images together with customizable fade ratio
- Resizes the dominant image to match the dimensions of the recessive image
- Saves the blended image to an output file

Usage:
1. Provide the paths to the dominant and recessive images.
2. Specify the output file path for the blended image.
3. Adjust the fade ratio to control the fading effect (0.0 - 1.0).
4. Run the program to generate the blended image.

Note: This program requires the PIL (Python Imaging Library) module.

Example:
fade_images("dominant_image.jpg", "recessive_image.jpg", "blended_image.jpg", 0.5)


