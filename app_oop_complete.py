import tkinter as tk
from tkinter import ttk
from windows_dpi import set_dpi_awarness

set_dpi_awarness()


# We can create our custom class which inherit from the base tk.Tk
class RootFrame(tk.Tk):
    def __init__(self):
        super().__init__()  # same as self = tk.Tk()
        self.title("Main Window")
        UserInputFrame(self).pack()


class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input = tk.StringVar()
        label = ttk.Label(self, text="Enter  your name: ")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self, text="Greet", command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")

    def greet(self):
        print(f"Hello, {self.user_input.get()} !")


root = RootFrame()
root.mainloop()
