import tkinter as tk
from tkinter import ttk
from windows_dpi import set_dpi_awarness

set_dpi_awarness()

root = tk.Tk()
root.title("Distance convertor")

root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

# Widget----
metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10)

feet_label = ttk.Label(main, text="Feet: ")
feet_output = ttk.Label(main, text="Feet shown here")

calculate_button = ttk.Button(main, text="Calculate")
# ---

# -- Layou
metres_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)
metres_input.grid(row=0, column=1, sticky="EW", padx=5, pady=5)

feet_label.grid(row=1, column=0, sticky="W", padx=5, pady=5)
feet_output.grid(row=1, column=1, sticky="EW", padx=5, pady=5)

calculate_button.grid(row=2, column=0, columnspan=2, sticky="EW", padx=5, pady=5)
# ---
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
