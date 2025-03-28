#Programmer: Timothy Pickering
#Date: 3/27/2025
#Title: Auto service calculator

#Required module
import tkinter as tk

#Dictionary to store services and their prices
services = {
    "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Fluid": 100.00,
    "Inspection": 35.00,
    "Muffler Replacement": 200.00,
    "Tire Rotation": 20.00,
    "Great Customer Service": 0.00
}

#Function to calculate total charges
def calculate_total():
    total = sum(price for service, price in services.items() if service_vars[service].get())
    label_total.config(text=f"Total Charges: ${total:.2f}")

#Create main application window
root = tk.Tk()
root.title("Joe's Automotive Services")
root.geometry("300x300")

#Create a dictionary to hold checkbutton variables
service_vars = {}

#Create checkbuttons for each service
for service, price in services.items():
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=f"{service} - ${price:.2f}", variable=var)
    chk.pack(anchor='w')
    service_vars[service] = var

#Button to calculate total
btn_calculate = tk.Button(root, text="Calculate Total", command=calculate_total)
btn_calculate.pack(pady=10)

#Label to display total
label_total = tk.Label(root, text="Total Charges: $0.00", font=("Arial", 12, "bold"))
label_total.pack()

#Start the tkinter event loop
root.mainloop()