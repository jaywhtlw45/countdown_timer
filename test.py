import tkinter as tk

root = tk.Tk()
root.title("Transparent Window Example")
root.geometry("300x200")

# Set a background color that will be made transparent
root.config(bg="red")

# Make the background color transparent
root.wm_attributes("-transparentcolor", "red")

# Create a label (or any other widget)
label = tk.Label(root, text="This is a transparent label",
                 bg="red", fg="white")
label.pack(pady=20)

root.mainloop()
