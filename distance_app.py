import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from windows_dpi import set_dpi_awarness

set_dpi_awarness()


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Convertor")
        frame = MetresToFeet(self, padding=(60, 30))
        frame.grid()

        # Key Bindings can be done on the root, metres input
        self.bind("<Return>", frame.calculate_feet)  # Enter key
        self.bind("<KP_Enter>", frame.calculate_feet)  # Key pad enter key


class MetresToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        # the variable to hold the calculation
        self.mtr_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet shown here")

        # Widget----
        metres_label = ttk.Label(self, text="Metres:")
        metres_input = ttk.Entry(self, width=10, textvariable=self.mtr_value, font=("Segoe UI", 15))

        feet_label = ttk.Label(self, text="Feet: ")
        feet_output = ttk.Label(self, textvariable=self.feet_value)

        calculate_button = ttk.Button(self, text="Calculate", command=self.calculate_feet)
        # ---
        # -- Layout
        metres_label.grid(row=0, column=0, sticky="W")
        metres_input.grid(row=0, column=1, sticky="EW")

        feet_label.grid(row=1, column=0, sticky="W")
        feet_output.grid(row=1, column=1, sticky="EW")

        calculate_button.grid(row=2, column=0, columnspan=2, sticky="EW")
        # ---

        # Performing the padx and pady operation on all the children of main window
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    # Function to fire up when event happens
    def calculate_feet(self, *args):
        """
        If the button is clicked before typing anything the value error will be thrown
        :param args:
        :return:
        """
        try:
            metres = float(self.mtr_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f"{feet : .3f}")
        except ValueError:
            pass


root = DistanceConverter()

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1)

root.mainloop()
