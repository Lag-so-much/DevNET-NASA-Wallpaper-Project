from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk
from PIL import Image, ImageTk
from wallpaper_utils import set_wallpaper , image_path, decodeapod, dimensions


root = tb.Window(themename="solar")
root.title("Nasa Picture of the Day")
root.geometry(dimensions)
root.attributes("-topmost", True)  # Make window always on top
myButton = Button(root)
root.resizable(False, False) # not resizable in both directions

#Set Fullscreen as root State
#root.state('zoomed')


# Filter Data For the GUI
title = decodeapod['title']




#Style
my_style = tb.Style()
my_style.configure('Default.TButton', font = ("Helvetica" , 18))


my_button=tb.Button(text="Set Wallpaper",
                   bootstyle ="default", command =  lambda : set_wallpaper(image_path), style = "Default.TButton")
    
my_button.place( x = 150, y = 850)

my_button2=tb.Button(text="Learn More",
                   bootstyle ="default", style = "Default.TButton")
my_button2.place( x = 500, y = 850)



custom_font = ("Helvetica", 25, "bold")
# Create a label widget
label = tk.Label(root, text= title, font = custom_font)

# Pack the label widget into the main window
label.place(x = 15 , y =0 )





def grab_image():
#Create a photoimage object of the image in the path
    image1 = Image.open(image_path)
    image1 = image1.resize((800, 800))
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
#Position image
    label1.place(x=0, y=50)
    
    
def main():
    grab_image()
    #config_buttons()
if __name__=="__main__":
    main()
    
