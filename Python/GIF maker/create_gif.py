from pathlib import Path
from PIL import Image
import imageio.v3 as iio

folder = Path(__file__).parent  # Get the directory of the current script

filenames = [
    "IMG_20261111_174249_1.jpg",
    "IMG_20261111_174249_2.jpg",
    "IMG_20261111_174249_3.jpg",
    "IMG_20261111_174249_4.jpg",
    "IMG_20261111_174249_5.jpg",
    "IMG_20261111_174249_6.jpg",
    "IMG_20261111_174249_7.jpg",
    "IMG_20261111_174249_8.jpg",
    "IMG_20261111_174249_9.jpg",
    "IMG_20261111_174249_10.jpg",
    "IMG_20261111_174249_11.jpg",
    "IMG_20261111_174249_12.jpg",
    "IMG_20261111_174249_13.jpg",
    "IMG_20261111_174249_14.jpg",
    "IMG_20261111_174249_15.jpg",
    "IMG_20261111_174249_16.jpg",
    "IMG_20261111_174249_17.jpg",
    "IMG_20261111_174249_18.jpg",
    "IMG_20261111_174249_19.jpg",
    "IMG_20261111_174249_20.jpg",
]  # List of image filenames

images = []  # List to store images

first_image = Image.open(folder / filenames[0])  # Open the first image to get its size
gif_size = first_image.size  # Get the size of the first image

for filename in filenames:
    image_path = folder / filename  # Create the full path to the image file

    image = Image.open(image_path)  # Open the image
    image = image.convert("RGBA")  # Convert image to RGBA format
    image = image.resize(gif_size)  # Resize image to match the size of the first image

    images.append(image)  # Add the processed image to the list

    if not image_path.exists():
        print(f"Warning: {image_path} does not exist. Skipping this file.")
        continue


if images:
    output_path = folder / "output.gif"  # Path for the output GIF
    iio.imwrite(output_path, images, duration=30, loop=0)  # Write images to
    print(f"GIF created successfully at: {output_path}")
else:
    print("No images were found to create a GIF.")
    
# IMPORTANT NOTICE:
# SAVE THIS FILE AFTER YOU HAVE SELECTED THE IMAGES YOU WANT TO USE FOR THE GIF. OTHERWISE, IT WILL NOT WORK.
# BASICALLY AFTER YOU INPUT THE IMAGE NAMES, SAVE THE FILE AND THEN RUN IT. OTHERWISE, IT WILL NOT WORK.

# To Run:
# Open PowerShell, in the terminal, press the arrow on the right of "+" and select Powershell. Then type the following command and press Enter:
# python ".\create_gif.py"

# To Find:
# Get-ChildItem -Filter *.png
# .png or any other file type you want to filter for.

# To Find w/o filter
# Get-ChildItem

# When Get-ChildItem is run:
#Mode                 LastWriteTime         Length Name                                                                                       
#----                 -------------         ------ ----                                                                                       
#-a----        30/10/2026   8:09 pm            957 create_gif.py                                                                              
#-a----        30/10/2026  11:59 am        2541016 Screenshot 2026-10-30 115954.png                                                           
#-a----        30/10/2026  12:00 pm        2469395 Screenshot 2026-10-30 120029.png                                                           

# Example: in 2469395 Screenshot 2026-10-30 120029.png
# Copy Paste ONLY the file name [Screenshot 2026-10-30 120029.png] and NOT the numbers before it [2469395]
# If done, then run:
# python ".\create_gif.py"

