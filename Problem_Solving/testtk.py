import tkinter as tk

# create a new tkinter window
window = tk.Tk()

# set the window title
window.title("My Window")

# create a label widget
label = tk.Label(window, text="Hello, tkinter!")

# pack the label widget into the window
label.pack()

# create a button widget
button = tk.Button(window, text="Click me!")

# pack the button widget into the window
button.pack()

# start the tkinter event loop
window.mainloop()
