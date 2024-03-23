from tkinter import * #GUI
from ttkbootstrap.constants import * #GUI
import ttkbootstrap as tb #GUI
import tkinter as tk #GUI
import pyttsx3 #Text to Speech
import os #operating system changes
from PIL import Image, ImageTk #importing images into tkinter and ttkbootstrap
from wallpaper_utils import set_wallpaper , image_path, decodeapod, dimensions #Wallpaper Functionality
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #hide welcome message from pygame
import pygame #import pygame

#define root window
root = tb.Window(themename="solar")

 # Filter Data For the GUI
title = decodeapod['title']
explanation = decodeapod ['explanation']

# Initialize mixer module in pygame
pygame.mixer.init()

def create_audio():
    # Set the full path for the audio file
    current_directory = os.getcwd()
    output_filename = "Image_audio.wav"
    engine = pyttsx3.init()
    engine.save_to_file(text= explanation, filename= output_filename)
    engine.runAndWait()
    return output_filename

output_filename = create_audio()

    
def play_audio():
    pygame.mixer.music.load(output_filename)
    pygame.mixer.music.play()

def stop_sound():
    pygame.mixer.music.stop()

def on_closing():
    stop_sound()
    root.destroy()

def grab_nasa_image():
#Create a photoimage object of the image in the path
    image1 = Image.open(image_path)
    image1 = image1.resize((800, 800))
    final_image = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image= final_image)
    label1.image = final_image
#Position image
    label1.place(x=0, y=50)
    
def place_sound_icon():
    sound_png = Image.open("speaker_Icon.png")
    sound_png = sound_png.resize((50, 50))
    final_sound_png = ImageTk.PhotoImage(sound_png)
    image_filename2 = os.path.basename('speaker_Icon.png')
    image_path2 = os.path.join(os.getcwd(), image_filename2)
    
    label1 = tk.Label(image=final_sound_png)
    label1.image = final_sound_png
#Position image
    label1.place(x=670, y=850)


def main():
    
    create_audio()
    root.title("Nasa Picture of the Day")
    root.geometry(dimensions)
    root.attributes("-topmost", True)  # Make window always on top
    root.resizable(False, False) # not resizable in both directions
    # Handle window closing event
    root.protocol("WM_DELETE_WINDOW", on_closing)

    #Set Fullscreen as root State
    #root.state('zoomed')



    #Configure GUI Style
    my_style = tb.Style()
    my_style.configure('Default.TButton', font = ("Helvetica" , 18))
    

    #Create GUI Buttons and Place them on Screen
    my_button=tb.Button(text="Set Wallpaper",
                   bootstyle ="default", command =  lambda : set_wallpaper(image_path), style = "Default.TButton")
    
    my_button.place( x = 150, y = 850)

    my_button2=tb.Button(text="Learn More",
                   bootstyle ="default", style = "Default.TButton" , command = lambda : play_audio())
    my_button2.place( x = 470, y = 850)


    #Create custom label font. 
    custom_font = ("Helvetica", 25, "bold")
    # Create a label widget
    label = tk.Label(root, text= title, font = custom_font, anchor ='center')

    # Pack the label widget into the main window
    label.pack()
    
    #Function Calls
    
    grab_nasa_image()
    place_sound_icon()
    

if __name__=="__main__":
    main()
    root.mainloop() #start main GUI
    