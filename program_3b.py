#Programmer: Timothy Pickering
#Date: 3/27/2025
#Title: User friendly phone service calculator

import tkinter as tk
from tkinter import messagebox
from datetime import datetime


#Function to convert time input to 24-hour format
def convert_to_24_hour(time_str, am_pm):
    time_obj = datetime.strptime(f"{time_str} {am_pm}", "%I:%M %p")
    return time_obj.hour, time_obj.minute


#Function to calculate call cost based on time range
def calculate_cost():
    try:
        #Get user input
        start_time = entry_start.get()
        start_am_pm = start_period.get()
        stop_time = entry_stop.get()
        stop_am_pm = stop_period.get()

        #Convert times to 24-hour format
        start_hour, start_minute = convert_to_24_hour(start_time, start_am_pm)
        stop_hour, stop_minute = convert_to_24_hour(stop_time, stop_am_pm)

        #Calculate total minutes of call duration
        start_total_minutes = start_hour * 60 + start_minute
        stop_total_minutes = stop_hour * 60 + stop_minute

        if stop_total_minutes <= start_total_minutes:
            messagebox.showerror("Input Error", "Stop time must be later than start time.")
            return

        total_minutes = stop_total_minutes - start_total_minutes
        daytime_minutes = evening_minutes = offpeak_minutes = 0
        cost_daytime = cost_evening = cost_offpeak = 0

        #Calculate cost based on different rate categories
        for minute in range(start_total_minutes, stop_total_minutes):
            hour = (minute // 60) % 24
            if 6 <= hour < 18:
                cost_daytime += 0.02
                daytime_minutes += 1
            elif 18 <= hour < 24:
                cost_evening += 0.12
                evening_minutes += 1
            else:
                cost_offpeak += 0.05
                offpeak_minutes += 1

        total_cost = cost_daytime + cost_evening + cost_offpeak

        #Display subtotal and total charge
        messagebox.showinfo("Call Cost", f"Daytime ({daytime_minutes} min): ${cost_daytime:.2f}\n"
                                         f"Evening ({evening_minutes} min): ${cost_evening:.2f}\n"
                                         f"Off-Peak ({offpeak_minutes} min): ${cost_offpeak:.2f}\n"
                                         f"--------------------------\n"
                                         f"Total cost: ${total_cost:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid time in HH:MM format.")


#Create main application window
root = tk.Tk()
root.title("Long-Distance Call Cost Calculator")
root.geometry("400x400")

#Display charge rates
label_rates = tk.Label(root,
                       text="Charge Rates:\nDaytime (6 AM - 5:59 PM): $0.02/min\nEvening (6 PM - 11:59 PM): $0.12/min\nOff-Peak (Midnight - 5:59 AM): $0.05/min")
label_rates.pack(pady=10)

#Start time input
label_start = tk.Label(root, text="Start Time (HH:MM):")
label_start.pack()
entry_start = tk.Entry(root)
entry_start.pack()
start_period = tk.StringVar(value="AM")
tk.OptionMenu(root, start_period, "AM", "PM").pack()

#Stop time input
label_stop = tk.Label(root, text="Stop Time (HH:MM):")
label_stop.pack()
entry_stop = tk.Entry(root)
entry_stop.pack()
stop_period = tk.StringVar(value="AM")
tk.OptionMenu(root, stop_period, "AM", "PM").pack()

#Button to calculate cost
tk.Button(root, text="Calculate Cost", command=calculate_cost).pack(pady=10)

#Start the Tkinter event loop
root.mainloop()