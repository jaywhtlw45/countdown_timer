import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading


def start_countdown():
    try:
        total_time = int(entry.get())
        countdown(total_time)
    except ValueError:
        label.config(text="Enter a valid number!")


def countdown(time_left):
    def update_timer():
        nonlocal time_left
        while time_left >= 0:
            mins, secs = divmod(time_left, 60)
            timer_text.set(f"{mins:02}:{secs:02}")
            time.sleep(1)
            time_left -= 1
        timer_text.set("Time's up!")

    thread = threading.Thread(target=update_timer, daemon=True)
    thread.start()


def resize_background(event):
    new_width, new_height = event.width, event.height
    canvas.config(width=new_width, height=new_height)  # Update canvas size

    # Reload original image to maintain quality
    original = Image.open("background.jpg")  # Reload from the source
    resized_image = original.resize((new_width, new_height), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)

    # Clear previous image before setting new one
    canvas.delete("bg")
    canvas.create_image(0, 0, image=bg_image, anchor='nw', tags="bg")

    # Keep reference to prevent garbage collection
    canvas.bg_image = bg_image




root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x300")
root.resizable(True, True)

# Load background image
image_path = "background.jpg"  # Change this to your image filename
original_image = Image.open(image_path)
resized_image = original_image.resize((400, 300), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(resized_image)

# Canvas for background
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor='nw')
canvas.bg_image = bg_image

# Countdown timer UI
frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

timer_text = tk.StringVar(value="00:00")
label = ttk.Label(frame, textvariable=timer_text, font=("Arial", 24))
label.pack()

entry = ttk.Entry(frame)
entry.pack()

start_button = ttk.Button(frame, text="Start", command=start_countdown)
start_button.pack()

# Bind resize event to adjust background
root.bind("<Configure>", resize_background)

root.mainloop()