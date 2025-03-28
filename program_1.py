#Programmer: Timothy Pickering
#Date: 3/27/2025
#Title: MPG calculator

#Required module
import tkinter as tk
from tkinter import messagebox

#Function to calculate MPG
def calculate_mpg():
    try:
        #Get user input from entry fields
        gallons = float(entry_gallons.get())
        miles = float(entry_miles.get())

        #Validate input
        if gallons <= 0 or miles <= 0:
            messagebox.showerror("Input Error", "Please enter positive values for both fields.")
            return

        #Perform MPG calculation
        mpg = miles / gallons

        #Display result in label
        label_result.config(text=f"Miles Per Gallon: {mpg:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


#Create main application window
root = tk.Tk()
root.title("MPG Calculator")
root.geometry("300x200")

#Label and entry for gallons
label_gallons = tk.Label(root, text="Gallons of Gas:")
label_gallons.pack()
entry_gallons = tk.Entry(root)
entry_gallons.pack()

#Label and entry for miles
label_miles = tk.Label(root, text="Miles Driven:")
label_miles.pack()
entry_miles = tk.Entry(root)
entry_miles.pack()

#Button to calculate MPG
tk.Button(root, text="Calculate MPG", command=calculate_mpg).pack(pady=10)

#Label to display results
label_result = tk.Label(root, text="")
label_result.pack()

#Start the tkinter event loop
root.mainloop()