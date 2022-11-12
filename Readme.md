## Simple converter feet to meter from official tk docu tutorial


#### 1. Program starts by incorporating Tk:

    from tkinter import *
    from tkinter import ttk

These two lines tell Python that the program needs two modules. The first, tkinter, is the standard binding to Tk. When imported, it loads the Tk library on your system. 
The second, ttk, is a submodule of tkinter. It implements Python's binding to the newer "themed widgets".

#### 2. Setting up the Main Application Window:
Next, the following code sets up the main application window, giving it the title "Feet to Meters."

    root = Tk()
    root.title("Feet to Meters")

#### 3. Creating a Content Frame
Next, we create a frame widget, which will hold the contents of our user interface.

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

After the frame is created, grid places it directly inside our main application window. The columnconfigure/rowconfigure bits tell Tk that the frame should expand to fill any extra space if the window is resized.

#### 4. Creating the Entry Widget
The first widget we'll create is the entry to input the number of feet to convert.

    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))

We need to do two things: create the widget itself and then place it onscreen.

When we create a widget, we need to specify its parent. That is the widget that the new widget will be placed inside. In this case, we want our entry placed inside the content frame. Our entry, and other widgets we'll create shortly, are said to be children of the content frame.

In Python the parent is passed as the first parameter when instantiating a widget object.

When we create a widget, we can optionally provide it with certain configuration options. Here, we specify how wide we want the entry to appear, i.e., 7 characters. We also assign it a mysterious textvariable; we'll see what that does shortly.

When widgets are created, they don't automatically appear on the screen; Tk doesn't know where you want them placed relative to other widgets. That's what the grid part does. Remember the layout grid when we sketched out our application? Widgets are placed in the appropriate column (1, 2, or 3) and row (also 1, 2, or 3).

The sticky option to grid describes how the widget should line up within the grid cell, using compass directions. So w (west) means to anchor the widget to the left side of the cell, we (west-east) means to attach it to both the left and right sides, and so on. Python also defines constants for these directional strings, which you can provide as a list, e.g. W or (W, E).

#### 5. Creating the Remaining Widgets
We then do exactly the same thing for the remaining widgets. We have one label that will display the resulting number of meters that we calculate. We have a "Calculate" button that is pressed to perform the calculation. Finally, we have three static text labels to make it clear how to use the application. For each of these widgets, we first create it and then place it onscreen in the appropriate cell in the grid.

    meters = StringVar()
    ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

    ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#### 6. Adding Some Polish
We then put a few finishing touches on our user interface.

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    feet_entry.focus()
    root.bind("<Return>", calculate)

The first part walks through all of the widgets contained within our content frame and adds a little bit of padding around each so they aren't so scrunched together. (We could have added these options to each grid call when we first put the widgets onscreen, but this is a nice shortcut.)

The second part tells Tk to put the focus on our entry widget. That way, the cursor will start in that field, so users don't have to click on it before starting to type.

The third line tells Tk that if a user presses the Return key (Enter on Windows), it should call our calculate routine, the same as if they pressed the Calculate button.

#### 7. Performing the Calculation
Speaking of which, here we define our calculate procedure. It's called when a user presses the Calculate button or hits the Return key. It performs the feet to meters calculation.

    def calculate(*args):
        try:
            value = float(feet.get())
            meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

 As you can clearly see, this routine takes the number of feet from our entry widget, does the calculation, and places the result in our label widget.

Say what? It doesn't look like we're doing anything with those widgets! Here's where the magic textvariable options we specified when creating the widgets come into play. We specified the global variable feet as the textvariable for the entry. Whenever the entry changes, Tk will automatically update the global variable feet. Similarly, if we explicitly change the value of a textvariable associated with a widget (as we're doing for meters which is attached to our label), the widget will automatically be updated with the current contents of the variable. For Python, the only caveat is that these variables must be an instance of the StringVar class. Slick.

```The multiplying and dividing by 10000.0 is to avoid the rounding problems inherent in floating-point math. A simple calculation, e.g., 0.3048*1.5, could result in a number like 0.45720000000000005, which would neither be correct or visually appealing when displayed. There are other ways to do this. of course.```

#### 8. Start the Event Loop

Finally, we need to tell Tk to enter its event loop, which is necessary for everything to appear onscreen and allow users to interact with it.

    root.mainloop()