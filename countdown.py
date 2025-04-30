import tkinter as tk
import time
import re
from PIL import Image, ImageTk

# create the main application window
root = tk.Tk()
root.title('Countdown Timer')
root.geometry('400x500')
root.configure(bg='lightblue')

# global var
prev_time_entry = 5
time_left = prev_time_entry
timer_job_id = None
new_start = True

font_family = "Arial"
size = 14
style = "" # options bold, italic, or bold italic

# background
bg_image = Image.open("./img/default/background/background.jpg")
bg_image = bg_image.resize((400, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



# updates the correct time in the timer
def update_timer_entry_display():
    global time_left
    timer_entry.config(state="normal")
    timer_entry.delete(0, tk.END)
    timer_entry.insert(0, f"{time_left//60}:{time_left % 60:02d}")
    timer_entry.config(state="readonly")

# timer entry widget
timer_entry = tk.Entry(root, font=(font_family,48), bg = "lightblue", justify = "center", bd=0, readonlybackground="lightblue")
timer_entry.pack(pady=(20,10))
update_timer_entry_display()
timer_entry.config(state="normal")

# notification frame widget
notification_frame = tk.Frame(root, bg='lightblue', height=60)
notification_frame.pack(side='bottom', fill='x', pady=10)
notification_frame.pack_propagate(False)

def push_notificaiton(message: str, font_color: str, duration=1000):
    global font_family
    note = tk.Label(notification_frame, text=message, font=(font_family, 12, "bold"), fg=font_color, bg="lightblue")
    note.pack(anchor="s", padx=10)
    note.after(duration, note.destroy)

def handle_invalid_time()->bool:
    print("invalid time")
    push_notificaiton("invalid time", "red")
    timer_entry.config(state='normal')
    return False

# validates user input from timer_entry widget and adjusts global time_left
def set_time()-> bool:
    global time_left, prev_time_entry
    entry = timer_entry.get()

    if not(is_valid_timer_string(entry)):
        return handle_invalid_time()
    
    minutes, seconds = map(int, entry.strip().split(":"))
    time_left = minutes*60 + seconds

    if time_left <=0:
        return handle_invalid_time()
    
    if new_start:
        prev_time_entry = time_left
    
    return True        

def is_valid_timer_string(s: str) -> bool:
    return bool(re.match(r'^\d{1,3}:\d{1,3}$', s))

def update_timer():
    global time_left, timer_job_id, new_start

    if time_left > 0:
        update_timer_entry_display()
        time_left -= 1
        timer_job_id = root.after(1000, update_timer)
    else:
        root.after_cancel(timer_job_id)
        timer_job_id = None
        
        update_timer_entry_display()
        timer_entry.config(state="normal")

def start_timer():
    global timer_job_id, prev_time_entry
    print('time_left:', time_left)
    print('prev_time_entry', prev_time_entry)

    if not timer_job_id:
        timer_entry.config(state="readonly")
        if (set_time()):
            print("set_time returns True")
            update_timer()
        else:
            print("set_time")

def stop_timer():
    global timer_job_id, new_start
    print(timer_job_id)
    if timer_job_id:
        root.after_cancel(timer_job_id)
        timer_job_id = None
        timer_entry.config(state="normal")
        new_start = False

def restart_timer():
    global new_start
    global timer_job_id, time_left, prev_time_entry
    if timer_job_id:
        root.after_cancel(timer_job_id)
        timer_job_id = None
        
        new_start = True
        time_left = prev_time_entry
        timer_entry.config(state="normal")
    
    
    time_left = prev_time_entry
    print("time_left:", time_left)
    update_timer_entry_display()
    start_timer()

# Button Frame
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10, side="top", fill = 'y' )

#bd=0 removes border
start_img = tk.PhotoImage(file="./img/default/buttons/start.png")
start_button = tk.Button(button_frame, image=start_img, bg="lightblue", activebackground="lightblue", command=start_timer, bd=0)
start_button.pack(padx='5', side="left")

stop_img = tk.PhotoImage(file="./img/default/buttons/stop.png")
stop_button = tk.Button(button_frame, image=stop_img, bg="lightblue", activebackground="lightblue", command=stop_timer, bd =0)
stop_button.pack(padx='5', side="left")

reset_img = tk.PhotoImage(file="./img/default/buttons/reset.png")
reset_button = tk.Button(button_frame, image=reset_img, bg="lightblue", activebackground="lightblue", command=restart_timer, bd=0)
reset_button.pack(padx='5', side = "left")



root.mainloop()


