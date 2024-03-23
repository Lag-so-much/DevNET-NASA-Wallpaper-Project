import urllib.request
import json
import os
import ctypes
from PIL import Image 

# Define API URL and key
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=Oc8HHWhhrnX888hP18AHrxQUTKZHJwP27CLw2maW'

# Fetch data from the API
apodurlobj = urllib.request.urlopen(apodurl + mykey)
apodread = apodurlobj.read()

# Decode JSON response
decodeapod = json.loads(apodread.decode('utf-8'))



def set_wallpaper(image_path):
    """Function to set wallpaper on Windows."""
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Wallpaper set successfully!")
    except Exception as e:
        print("Error occurred while setting wallpaper:", e)

def download_image():
    """Function to download an image and return its path."""
    image_url = decodeapod['url']
    image_filename = os.path.basename(image_url)
    image_path = os.path.join(os.getcwd(), image_filename)
    urllib.request.urlretrieve(image_url, image_path)
    return image_path

image_path = download_image()

# Open the image
nasa_img = Image.open(image_path)

# Get the original image width and height
image_width = nasa_img.width
image_height = nasa_img.height

# Calculate the dimensions, subtracting 160 from width and adding 230 to height
adjusted_width = min(image_width - 160, 835)
adjusted_height = min(image_height + 230, 920)  # Ensure height doesn't exceed 920

# Format the dimensions string
dimensions = "{}x{}".format(adjusted_width, adjusted_height)




