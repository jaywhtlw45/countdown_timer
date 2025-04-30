import tkinter as tk
import time
import re

# create the main application window
root = tk.Tk()
root.title('Countdown Timer')
root.geometry('400x300')
root.configure(bg='lightblue')

# global var
prev_time_entry = 5
time_left = prev_time_entry
timer_job_id = None

# updates the correct time in the timer
def update_timer_entry_display():
    global time_left
    timer_entry.config(state="normal")
    timer_entry.delete(0, tk.END)
    timer_entry.insert(0, f"{time_left//60}:{time_left % 60:02d}")
    timer_entry.config(state="readonly")

#Create the timer label
timer_entry = tk.Entry(root, font=("Helvetica",48), bg = "lightblue", justify = "center")
timer_entry.pack(pady=20)
update_timer_entry_display()
timer_entry.config(state="normal")

# validates user input from timer_entry widget and adjusts global time_left
def update_time_left_from_input()-> bool:
    global time_left, prev_time_entry
    entry = timer_entry.get()

    if is_valid_timer_string(entry):
        minutes, seconds = map(int, entry.strip().split(":"))
        time_left = minutes * 60 + seconds

        # when reset button is presssed the previous time that was entered by user will be used
        prev_time_entry = time_left
        return True
    
    return False

def is_valid_timer_string(s: str) -> bool:
    pattern = r'^\d{1,3}:\d{1,3}$'
    return bool(re.match(pattern, s))


def update_timer():
    global time_left, timer_job_id

    if time_left > 0:
        update_timer_entry_display()
        time_left -= 1
        timer_job_id = root.after(1000, update_timer)

    else:
        root.after_cancel(timer_job_id)
        timer_job_id = None
        
        update_timer_entry_display()
        timer_entry.config(state="normal")

        # when restart event occurs use the last entry from the user
        time_left = prev_time_entry


def start_timer():
    global timer_job_id
    print('start_timer()', timer_job_id)

    if not timer_job_id:
        timer_entry.config(state="readonly")
        update_time_left_from_input()
        update_timer()

def stop_timer():
    global timer_job_id
    print(timer_job_id)
    if timer_job_id:
        root.after_cancel(timer_job_id)
        timer_job_id = None
        timer_entry.config(state="normal")

def restart_timer():
    global timer_job_id, time_left, prev_time_entry
    if timer_job_id:
        root.after_cancel(timer_job_id)
        timer_job_id = None
    
    time_left = prev_time_entry
    update_timer_entry_display()
    start_timer()


start_button = tk.Button(root, text = "Start", font = ("Helvetica",14), command=start_timer)
start_button.pack(pady='5')

stop_button = tk.Button(root, text="Stop Button", font =("Helvetica", 14), command=stop_timer)
stop_button.pack(pady='5')

reset_button = tk.Button(root, text="Reset Button", font = ("Helvetica", 14), command=restart_timer)
reset_button.pack(pady='5')

# start the tkinter event loop
root.mainloop()


