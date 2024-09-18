import tkinter as tk
from tkinter import messagebox
import time
import threading

# Function to set the alarm
def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    messagebox.showinfo("Alarm Set", f"Alarm is set for {alarm_time}")
    while True:
        time.sleep(1)
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Time to wake up!")
            break

# Function to start the alarm in a new thread
def start_alarm():
    t = threading.Thread(target=set_alarm)
    t.start()

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Set window size
root.geometry("400x200")

# Create and place the labels and inputs for the alarm time
tk.Label(root, text="Set Time for Alarm (24-hour format):").pack(pady=10)
tk.Label(root, text="Hour").pack()
hour = tk.Entry(root, width=5)
hour.pack()

tk.Label(root, text="Minute").pack()
minute = tk.Entry(root, width=5)
minute.pack()

tk.Label(root, text="Second").pack()
second = tk.Entry(root, width=5)
second.pack()

# Set Alarm button
tk.Button(root, text="Set Alarm", command=start_alarm).pack(pady=20)

# Run the main loop
root.mainloop()
