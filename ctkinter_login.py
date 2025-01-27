from customtkinter import *
from PIL import Image
import pygame
from tkinter import messagebox
import os

app = CTk()
app.geometry("400x600")

pygame.mixer.init()

current_directory = os.path.dirname(os.path.abspath(__file__))

image1_path = os.path.join(current_directory, 'image1.jpg')
image2_path = os.path.join(current_directory, 'image2.jpg')
music_path = os.path.join(current_directory, 'music.mp3')
music2_path = os.path.join(current_directory, 'music2.mp3')
music3_path = os.path.join(current_directory, 'music3.mp3')

def login():
    if entry_login.get() == "admin" and entry_password.get() == "admin":
        messagebox.showinfo("Login", "Login successful", parent=app)
        frame.place_forget()  
        kafelki()  
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

def play_music1():
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(loops=-1, start=0.0)

def play_music2():
    pygame.mixer.music.load(music2_path)
    pygame.mixer.music.play(loops=-1, start=0.0)

def play_music3():
    pygame.mixer.music.load(music3_path)
    pygame.mixer.music.play(loops=-1, start=0.0)

def kafelki():
    tile_frame = CTkFrame(app, fg_color="#A717E0", border_color="#753C8B", border_width=3, width=350, height=300)
    tile_frame.place(relx=0.5, rely=0.5, anchor="center")

    btn_music1 = CTkButton(tile_frame, text="Play Song 1", command=play_music1)
    btn_music1.pack(pady=10, padx=10)

    btn_music2 = CTkButton(tile_frame, text="Play Song 2", command=play_music2)
    btn_music2.pack(pady=10, padx=10)

    btn_music3 = CTkButton(tile_frame, text="Play Song 3", command=play_music3)
    btn_music3.pack(pady=10, padx=10)
    
image1 = CTkImage(light_image=Image.open(image2_path), size=(400, 600))
image2 = CTkImage(light_image=Image.open(image1_path), size=(400, 600))

my_label = CTkLabel(app, image=image1)
my_label.place(relx=0.5, rely=0.5, anchor="center")

set_appearance_mode("dark")

frame = CTkFrame(app, fg_color="#A717E0", border_color="#753C8B", border_width=3, width=300, height=200)
frame.place(relx=0.5, rely=0.5, anchor="center")

entry_login = CTkEntry(frame, placeholder_text="Enter Username")
entry_login.pack(pady=5, padx=10)

entry_password = CTkEntry(frame, show="*", placeholder_text="Enter Password")
entry_password.pack(pady=5, padx=10)

btn = CTkButton(frame, text="Log in", command=login)
btn.pack(pady=5)
switch = CTkSwitch(app, text="Change background theme", command=change_theme)
switch.place(relx=0.5, rely=0.7, anchor="center")

slider = CTkSlider(app, from_=0, to=100, command=music)
slider.place(relx=0.5, rely=0.8, anchor="center")

pygame.mixer.music.load(music_path)
pygame.mixer.music.play(loops=-1, start=0.0)

app.mainloop()
