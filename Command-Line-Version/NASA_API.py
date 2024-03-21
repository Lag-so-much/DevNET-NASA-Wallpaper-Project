import urllib.request
import json
import webbrowser
import os
import ctypes

def set_wallpaper(image_path):
    """Function to set wallpaper on Windows."""
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Wallpaper set successfully!")
    except Exception as e:
        print("Error occurred while setting wallpaper:", e)


# Define API URL and key
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=Oc8HHWhhrnX888hP18AHrxQUTKZHJwP27CLw2maW'

# Fetch data from the API
apodurlobj = urllib.request.urlopen(apodurl + mykey)
apodread = apodurlobj.read()

# Decode JSON response
decodeapod = json.loads(apodread.decode('utf-8'))

# Print information about the APOD
print("\n\nConverted python data")
print(decodeapod)

# Prompt user to open the NASA Picture of the Day in their search engine
input('\nPress Enter to open NASA Picture of the Day in your search engine')
webbrowser.open(decodeapod['url'])

# Prompt user to set the fetched image as their wallpaper
set_wallpaper_option = input('\nDo you want to set the fetched image as your wallpaper? (yes/no): ')

if set_wallpaper_option.lower() in ['yes', 'Yes', 'y']:
    # Download the image
    image_url = decodeapod['url']
    image_filename = os.path.basename(image_url)
    image_path = os.path.join(os.getcwd(), image_filename)
    print (image_path)
    urllib.request.urlretrieve(image_url, image_path)

    # Set the image as wallpaper
    set_wallpaper(image_path)
else:
    quit
