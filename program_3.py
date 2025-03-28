#Programmer: Timothy Pickering
#Date: 3/27/2025
#Title: Phone service calculator

import tkinter as tk
from tkinter import messagebox

#Function to calculate call cost
def calculate_cost():
    try:
        minutes = float(entry_minutes.get())
        if minutes <= 0:
            messagebox.showerror("Input Error", "Please enter a positive number of minutes.")
            return

        #Determine rate based on selected category
        if rate_var.get() == "daytime":
            rate = 0.02
        elif rate_var.get() == "evening":
            rate = 0.12
        else:
            rate = 0.05

        #Calculate total cost
        total_cost = minutes * rate

        #Display result in message box
        messagebox.showinfo("Call Cost", f"Total Charge: ${total_cost:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")


#Create main application window
root = tk.Tk()
root.title("Long-Distance Call Cost Calculator")
root.geometry("350x250")

#Label and entry for minutes
label_minutes = tk.Label(root, text="Enter call duration (minutes):")
label_minutes.pack()
entry_minutes = tk.Entry(root)
entry_minutes.pack()

#Rate category selection using radio buttons
rate_var = tk.StringVar(value="daytime")  # Default selection

frame_rates = tk.LabelFrame(root, text="Select Rate Category")
frame_rates.pack(pady=10)

#Radio buttons for rate selection
tk.Radiobutton(frame_rates, text="Daytime (6:00 AM - 5:59 PM)", variable=rate_var, value="daytime").pack(anchor="w")
tk.Radiobutton(frame_rates, text="Evening (6:00 PM - 11:59 PM)", variable=rate_var, value="evening").pack(anchor="w")
tk.Radiobutton(frame_rates, text="Off-Peak (Midnight - 5:59 AM)", variable=rate_var, value="offpeak").pack(anchor="w")

#Button to calculate cost
tk.Button(root, text="Calculate Cost", command=calculate_cost).pack(pady=10)

#Start the Tkinter event loop
root.mainloop()
