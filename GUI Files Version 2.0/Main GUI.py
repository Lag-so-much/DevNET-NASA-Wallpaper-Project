from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkinter as tk
import pyttsx3
import os
from PIL import Image, ImageTk
import pygame

# Initialize mixer module in pygame
pygame.mixer.init()

# Define root window
root = tb.Window(themename="solar")

# Sample image path (replace this with your actual image path)
image_path = "sample_image.jpg"

# Filter Data For the GUI
title = "Sample Title"
explanation = "Sample Explanation"

def create_audio():
    # Sample implementation for demonstration purposes
    output_filename = "Image_audio.wav"
    return output_filename

def play_audio():
    pygame.mixer.music.load(create_audio())
    pygame.mixer.music.play()

def stop_sound():
    pygame.mixer.music.stop()

def on_closing():
    stop_sound()
    root.destroy()

def grab_nasa_image():
    # Sample implementation for demonstration purposes
    # This function should download the image from a URL or load it from a file
    # For demonstration, we'll just load a sample image
    global image_path
    image_path = "sample_image.jpg"

def place_sound_icon():
    try:
        sound_png = Image.open("speaker_Icon.png")
        sound_png = sound_png.resize((50, 50))
        final_sound_png = ImageTk.PhotoImage(sound_png)

        label_sound_icon = tk.Label(root, image=final_sound_png)
        label_sound_icon.image = final_sound_png
        label_sound_icon.place(x=670, y=850)

    except FileNotFoundError:
        print("Error: speaker_Icon.png not found.")

def main():
    root.title("Nasa Picture of the Day")
    root.geometry("800x900")
    root.attributes("-topmost", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)

    my_style = tb.Style()
    my_style.configure('Default.TButton', font=("Helvetica", 18))

    my_button = tb.Button(text="Set Wallpaper", bootstyle="default", command=grab_nasa_image, style="Default.TButton")
    my_button.place(x=150, y=850)

    my_button2 = tb.Button(text="Learn More", bootstyle="default", style="Default.TButton", command=play_audio)
    my_button2.place(x=470, y=850)

    custom_font = ("Helvetica", 25, "bold")
    label = tk.Label(root, text=title, font=custom_font)
    label.place(x=15, y=0)

    place_sound_icon()

    root.mainloop()

if __name__ == "__main__":
    main()
