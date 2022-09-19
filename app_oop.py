import tkinter as tk
from tkinter import ttk
from windows_dpi import set_dpi_awarness

set_dpi_awarness()


# We can create our custom class which inherit from the base tk.Tk
class RootFrame(tk.Tk):
    def __init__(self):
        super().__init__()  # same as self = tk.Tk()
        self.title("Main Window")
        ttk.Label(self, text="Your app").pack()


root = RootFrame()  # RootFrame is called which internally calls the Tk constructor the self is the current object
# we are referring to which is root.
root.mainloop()
