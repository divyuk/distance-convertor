import tkinter as tk
from tkinter import ttk
from windows_dpi import set_dpi_awarness

set_dpi_awarness()


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


root = tk.Tk()
my_frame = UserInputFrame(root)
my_frame.pack()
# label = ttk.Label(my_frame, text="Enter :")
# label.pack()

# Frame without class
# frame = ttk.Frame(root)
# label = ttk.Label(frame, text="Enter :")
# label.pack()

root.mainloop()
