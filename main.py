import time
import tkinter as tk


def tick():
    # get the current time from the computer
    current_time = time.strftime("%H:%M:%S")

    clock.config(text=current_time)
    clock.after(200, tick)


root = tk.Tk()
clock = tk.Label(root, font=("arial", 20, "bold"), bg="black", fg="green")
clock.pack(fill="both", expand=1)
tick()
root.mainloop()
