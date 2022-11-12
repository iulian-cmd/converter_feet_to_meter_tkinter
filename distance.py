from tkinter import *   # Import tkinter
from tkinter import ttk  # Create instance


def calculate(*args):   # Convert input to meters
    try:
        value = float(feet.get())  # Get the value from the feet entry box
        meters.set(int(0.3048 * value * 10000.0 + 0.5) /
                   10000.0)  # Convert to meters
    except ValueError:
        pass


root = Tk()  # Create an instance
root.title("Feet to Meters")  # Set the title

mainframe = ttk.Frame(root, padding="3 3 12 12")    # Create a frame
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))    # Set the frame
root.columnconfigure(0, weight=1)   # Set the column
root.rowconfigure(0, weight=1)  # Set the row

feet = StringVar()      # Create a string variable
# Create an entry box
feet_entry = ttk.Entry(mainframe, width=8, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))     # Set the entry box

meters = StringVar()    # Create a string variable
ttk.Label(mainframe, textvariable=meters).grid(
    column=2, row=2, sticky=(W, E))  # Create a label

ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W)  # Create a button

ttk.Label(mainframe, text="feet").grid(
    column=3, row=1, sticky=W)   # Create a label
ttk.Label(mainframe, text="is equivalent to").grid(
    column=1, row=2, sticky=E)   # Create a label
ttk.Label(mainframe, text="meters").grid(
    column=3, row=2, sticky=W)   # Create a label

for child in mainframe.winfo_children():    # Set the padding
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()  # Set the focus
root.bind("<Return>", calculate)    # Bind the enter key

root.mainloop()  # Start the main loop
