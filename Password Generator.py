import string
import random
import time
import sys
import os
import tkinter as tk
import tkinter.font as tkfont
import customtkinter
import pyperclip
from tkinter import * 
from tkinter.ttk import *

# Copy function
def clipboard_copy():
    copy_button.configure(image=clipboard_overlay, state=DISABLED)
    copied_notification.place(rely=0.900)
    get_password = result_label.cget("text")
    remove_lines = get_password.replace("\n", "")
    pyperclip.copy(remove_lines)
    password_str = pyperclip.paste()
    window.after(500, configure_copy_button)
def configure_copy_button():
    copy_button.configure(image=clipboard, state=NORMAL)
    window.after(1000, configure_toast)
def configure_toast():
    copied_notification.place(rely=1.5)

# Generate random password
def generate_password():
    # Get the desired password length from the scale widget
    length = int(slider_length.get())

    # Get the desired character sets from the checkboxes
    choices = []
    if upper_var.get():
        choices.extend(string.ascii_uppercase)
    if lower_var.get():
        choices.extend(string.ascii_lowercase)
    if digits_var.get():
        choices.extend(string.digits)
    if symbols_var.get():
        choices.extend(string.punctuation)

    # Generate the password
    global password
    password = "".join(random.choices(choices, k=length))

    # Display the password in the result label
    result_label.configure(text=password)
    get_slider_value = int(slider_length.get())
    slider = f"LENGTH {get_slider_value}"
    length_label.configure(text=slider)

    if len(password) > 20 and len(password) <= 41:
        first_div, sec_div = password[0:20], password[20:40]
        first_utilize = (f"{first_div}\n{sec_div}")      
        pass_frame1.place(relx=0.5, rely=0.142, anchor="center",width=310,height=55)
        result_label.configure(text=first_utilize , font=("Apercu Mono Pro", 20))
        result_label.place(relx=0.5, rely=0.145, anchor="center")
        strength_text.place(relx=0.060, rely=0.232, anchor="w")
        progressbar.place(relx=0.5, rely=0.210, anchor="center")

    elif len(password) >= 42:
        third_div, fourth_div, fifth_div = password[0:20], password[20:40], password[40:64]
        second_utilize = (f"{third_div}\n{fourth_div}\n{fifth_div}")  
        pass_frame1.place(relx=0.5, rely=0.166, anchor="center",width=310,height=80)
        result_label.configure(text=second_utilize,font=("Apercu Mono Pro", 18))
        result_label.place(relx=0.5, rely=0.165, anchor="center")
        strength_text.place(relx=0.060, rely=0.276, anchor="w")
        progressbar.place(relx=0.5, rely=0.255, anchor="center")
    else:
        pass_frame1.place(relx=0.5, rely=0.125, anchor="center",width=310,height=35)
        result_label.configure(text=password, font=("Apercu Mono Pro", 20))
        result_label.place(relx=0.5, rely=0.125, anchor="center")
        strength_text.place(relx=0.060, rely=0.197, anchor="w")
        progressbar.place(relx=0.5, rely=0.175, anchor="center")

    if len(password) < 12:
        progressbar.set(0.8)
        window.update_idletasks()
        strength_text.configure(text="Now that's a strong password!")
        if len(password) <= 10:
            progressbar.set(0.6)
            strength_text.configure(text="It's just short of great!")
            progressbar.configure(progress_color="#e3624e")
            if len(password) < 7:
                progressbar.set(0.4)
                strength_text.configure(text="Good start, but we can make it stronger.")
                progressbar.configure(progress_color="#f80032")

    else:
        progressbar.set(1)
        progressbar.configure(progress_color="#42a26e")

from PIL import Image, ImageTk

# Variables
window = customtkinter.CTk()
width = 350 # Width 
height = 560 # Height

# Assets
clipboard= customtkinter.CTkImage(Image.open("assets/clipboard.png"), size=(30, 30))
clipboard_overlay = customtkinter.CTkImage(Image.open("assets/clipboard_overlay.png"), size=(30, 30))
copied = customtkinter.CTkImage(Image.open("assets/notification.png"), size=(278, 50))

# Main Window & background
window.title("Password Generator")
window.iconbitmap("assets/lock.ico")
upper_bg = customtkinter.CTkCanvas(window,bg="#D9E6E9")
upper_bg.place(x=-1,y=-1,width=370,height=255)

# Grey line
lower_line = customtkinter.CTkFrame(window, fg_color="#d7d8d8")
lower_line.place(x=15,y=325,width=320,height=2)

# Password generate background
pass_frame1 = customtkinter.CTkFrame(master=window, fg_color="white", corner_radius=5)
pass_frame1.place(relx=0.5, rely=0.125, anchor="center",width=310,height=35)

# Set window to unresizable
window.resizable(False, False)


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

# Make window to appear middle of the screen
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

# Password scaler(slider)
slider_length = customtkinter.CTkSlider(master=window, from_=4, to=64, number_of_steps=64, orientation=customtkinter.HORIZONTAL, progress_color="#256674", button_color="#256674", button_hover_color="#143941", fg_color="#d9dfe0", width=320)
slider_length.set(12)


# Additional texts
length_label = customtkinter.CTkLabel(master=window, text=f"LENGTH 12", font=("sans-serif", 11), text_color="#3E5D64")
minimum_slider_value = customtkinter.CTkLabel(master=window, text="4", font=("", 14),text_color="grey", width=2, height=2)
maximum_slider_value = customtkinter.CTkLabel(master=window, text="64", font=("", 14),text_color="grey", width=2, height=2)
strength_text = customtkinter.CTkLabel(master=window, text="Ultimate password strength reached!", text_color="#212D37", fg_color="#D9E6E9")
copied_notification = customtkinter.CTkLabel(master=window, text="", image=copied, width=32, height=15)

# progressbar
progressbar = customtkinter.CTkProgressBar(master=window, progress_color="#42a26e", fg_color="#a1c2c8", width=310, height=5)
progressbar.set(1)

# Checkboxes(Uppercase Letters|Lowercase Letters|Digits|Symbols)
upper_var = tk.IntVar()
upper_check = customtkinter.CTkCheckBox(master=window, text="Uppercase letters", variable=upper_var, fg_color="#1b6272", hover_color="False", checkbox_width=21, checkbox_height=21, corner_radius=5, border_width=1, border_color="#bfbfbf")
upper_var.set(1)

lower_var = tk.IntVar()
lower_check = customtkinter.CTkCheckBox(master=window, text="Lowercase letters", variable=lower_var, fg_color="#1b6272", hover_color="False", checkbox_width=21, checkbox_height=21, corner_radius=5, border_width=1, border_color="#bfbfbf")
lower_var.set(1)

digits_var = tk.IntVar()
digits_check = customtkinter.CTkCheckBox(master=window, text="Digits", variable=digits_var, fg_color="#1b6272", hover_color="False", checkbox_width=21, checkbox_height=21, corner_radius=5, border_width=1, border_color="#bfbfbf")
digits_var.set(1)

symbols_var = tk.IntVar()
symbols_check = customtkinter.CTkCheckBox(master=window, text="Symbols", variable=symbols_var, fg_color="#1b6272", hover_color="False", checkbox_width=21, checkbox_height=21, corner_radius=5, border_width=1, border_color="#bfbfbf")

# Create generate button
generate_button = customtkinter.CTkButton(master=window, command=generate_password, text="Generate", font=("Open Sans Semibold", 14), fg_color="#1b6272", hover_color="#144b57",width=64, height=32, corner_radius=5)
generate_button.pack()

# Create copy button
copy_button = customtkinter.CTkButton(master=window, text="", image=clipboard, command=clipboard_copy, fg_color="#D9E6E9", hover=False, width=12, height=12)
copy_button.pack()

# Create the result label (for password)
result_label = customtkinter.CTkLabel(window, text="", fg_color="white", font=("Apercu Mono Pro", 20))

# All widgets positions
result_label.place(relx=0.5, rely=0.125, anchor="center") # result

minimum_slider_value.place(relx=0.060, rely=0.555, anchor="w") # text 4
maximum_slider_value.place(relx=0.900, rely=0.555, anchor="w") # text 64
strength_text.place(relx=0.060, rely=0.197, anchor="w") # text strength
length_label.place(relx=0.060, rely=0.485, anchor="w") # text length of the password
copied_notification.place(relx=0.1, rely=1.50, anchor="w") # toast notification

slider_length.place(relx=0.5, rely=0.525, anchor="center") # slider
progressbar.place(relx=0.5, rely=0.175, anchor="center") # progressbar

upper_check.place(relx=0.045, rely=0.635, anchor="w") # uppercase checkbox
lower_check.place(relx=0.045, rely=0.685, anchor="w") # lower checkbox
digits_check.place(relx=0.045, rely=0.735, anchor="w") # digits checkbox
symbols_check.place(relx=0.045, rely=0.785, anchor="w") # symbols checkbox

generate_button.place(relx=0.5, rely=0.350, anchor="center") # generate button
copy_button.place(relx=0.670, rely=0.350, anchor="center")# copy button

# Show random password at the startup
def start_password():
    chars = []
    chars[:0] = string.ascii_uppercase+string.ascii_lowercase+string.digits
    start_pass = "".join(random.choices(chars, k=12))
    result_label.configure(text=start_pass)
start_password()

# Main loop
window.mainloop()

# I'm not good at making variables, LOL