from customtkinter import *
from PIL import Image
import pygame  # Import pygame for music control
from tkinter import messagebox
import os  # To handle relative paths

app = CTk()
app.geometry("400x600")

# Initialize pygame mixer for music
pygame.mixer.init()

# Get the current directory (the folder where the script is running)
current_directory = os.path.dirname(os.path.abspath(__file__))

image1_path = os.path.join(current_directory, 'image1.jpg')
image2_path = os.path.join(current_directory, 'image2.jpg')
music_path = os.path.join(current_directory, 'music.mp3')

def login():
    if entry_login.get() == "admin" and entry_password.get() == "admin":
        messagebox.showinfo("Login", "Login successful", parent=app)
    else:
        messagebox.showerror("Login", "Login failed", parent=app)

def change_theme():
    if switch.get() == 1:
        my_label.configure(image=image1)
    else:
        my_label.configure(image=image2)

def music(value):
    volume = float(value) / 100  
    pygame.mixer.music.set_volume(volume) 

# Set up images for background
image1 = CTkImage(light_image=Image.open(image2_path), size=(400, 600))
image2 = CTkImage(light_image=Image.open(image1_path), size=(400, 600))

# Label for background image
my_label = CTkLabel(app, image=image1)
my_label.place(relx=0.5, rely=0.5, anchor="center")

set_appearance_mode("dark")

# Frame for login fields
frame = CTkFrame(app, fg_color="#A717E0", border_color="#753C8B", border_width=3, width=300, height=200)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Entry fields for username and password inside the frame
entry_login = CTkEntry(frame, placeholder_text="Enter Username")
entry_login.pack(pady=5, padx=10)

entry_password = CTkEntry(frame, show="*", placeholder_text="Enter Password")
entry_password.pack(pady=5, padx=10)

# Login button inside the frame, placed below the password entry field
btn = CTkButton(frame, text="Log in", command=login)
btn.pack(pady=5)

# Switch for theme change (outside the frame)
switch = CTkSwitch(app, text="Change background theme", command=change_theme)
switch.place(relx=0.5, rely=0.7, anchor="center")

# Slider for volume control (outside the frame)
slider = CTkSlider(app, from_=0, to=100, command=music)
slider.place(relx=0.5, rely=0.8, anchor="center")

# Play music
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(loops=-1, start=0.0)  

# Run the app
app.mainloop()
