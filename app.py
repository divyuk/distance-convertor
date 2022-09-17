import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from windows_dpi import set_dpi_awarness

set_dpi_awarness()

root = tk.Tk()
root.title("Distance convertor")

font.nametofont("TkDefaultFont").configure(size = 15)

root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

# the variable to hold the calculation
mtr_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")


# Function to fire up when event happens
def calculate_feet(*args):
    """
    If the button is clicked before typing anything the value error will be thrown
    :param args:
    :return:
    """
    try:
        metres = float(mtr_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet : .3f}")
    except ValueError:
        pass


# Widget----
metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, textvariable=mtr_value, font=("Segoe UI" , 15))

feet_label = ttk.Label(main, text="Feet: ")
feet_output = ttk.Label(main, textvariable=feet_value)

calculate_button = ttk.Button(main, text="Calculate", command=calculate_feet)
# ---

# -- Layout
metres_label.grid(row=0, column=0, sticky="W", padx=15, pady=15)
metres_input.grid(row=0, column=1, sticky="EW", padx=15, pady=15)

feet_label.grid(row=1, column=0, sticky="W", padx=15, pady=15)
feet_output.grid(row=1, column=1, sticky="EW", padx=15, pady=15)

calculate_button.grid(row=2, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
# ---

# Key Bindings can be done on the root, metres input
root.bind("<Return>", calculate_feet)  # Enter key
root.bind("<KP_Enter>", calculate_feet)  # Key pad enter key

root.mainloop()

"""
The Flow of code while writing
1) Import libraries
2)) Setup the frames
3) Setup the widgets
4) Setup the Layout
5) Tune the style using sticky property
6) Do Expansion using ColumnConfigure
"""
