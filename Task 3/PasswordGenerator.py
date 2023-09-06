from tkinter import *
import random
from PIL import Image, ImageTk


PRIMARY_COLOR = "#4A90E2"
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#333333"


def generate_password():
    password_field.delete(0, END)

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    max_length = int(password_length_input.get())

    nr_letters = random.randint(1, max_length - 2)
    nr_symbols = random.randint(1, max_length - nr_letters - 1)
    nr_numbers = max_length - nr_letters - nr_symbols

    password_list = []
    password_list.extend(random.choice(letters) for _ in range(nr_letters))
    password_list.extend(random.choice(symbols) for _ in range(nr_symbols))
    password_list.extend(random.choice(numbers) for _ in range(nr_numbers))
    random.shuffle(password_list)

    new_pass = ''.join(password_list)
    password_field.insert(0, new_pass)


window = Tk()
window.title("Password Generator App")
window.config(bg=BACKGROUND_COLOR)
window.geometry("600x450")
window.minsize(width=600, height=400)


title_label = Label(text="Password Generator", bg=BACKGROUND_COLOR, fg=PRIMARY_COLOR, font=("Helvetica", 36, 'bold'))
title_label.pack(pady=(20, 30))


input_frame = Frame(bg=BACKGROUND_COLOR)
input_frame.pack()

Label(input_frame, text="Password Length:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Helvetica", 16)).grid(row=0, column=0, sticky='w')
password_length_input = Spinbox(input_frame, from_=4, to=50, width=3, font=("Helvetica", 16))
password_length_input.grid(row=0, column=1, padx=10)
password_length_input.delete(0, "end")
password_length_input.insert(0, "12")


generate_button = Button(text="Generate Password", bg=PRIMARY_COLOR, fg=BACKGROUND_COLOR, font=("Helvetica", 16, 'bold'), command=generate_password)
generate_button.pack(pady=40)


password_field = Entry(width=30, font=("Helvetica", 20), fg=PRIMARY_COLOR)
password_field.pack(pady=30)


try:
    image = Image.open("C:/Users/acer/Pictures/FASHION/lock.jpg")
    image = image.resize((120, 140))
    image = ImageTk.PhotoImage(image)
    image_label = Label(image=image, bg=BACKGROUND_COLOR)
    image_label.place(x=35, y=95)
except Exception as e:
    print(f"Error loading image: {e}")

window.mainloop()
