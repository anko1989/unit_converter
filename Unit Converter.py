import tkinter as tk
from tkinter import ttk

conversion_map = {
    "miles": {"kilometers": lambda x: x * 1.60934},
    "kilometers": {"miles": lambda x: x / 1.60934},
    "pounds": {"kilograms": lambda x: x * 0.453592},
    "kilograms": {"pounds": lambda x: x / 0.453592}
}


def update_to_units(event):
    selected_unit = unit_from_var.get()
    if selected_unit in conversion_map:
        combo_to['values'] = list(conversion_map[selected_unit].keys())
        combo_to.set("")
    else:
        combo_to['values'] = []
        combo_to.set("")


def convert():
    unit_from = unit_from_var.get()
    unit_to = unit_to_var.get()
    try:
        value = float(entry_value.get())
    except ValueError:
        label_result.config(text="Please enter a valid number.")
        return

    if unit_from in conversion_map and unit_to in conversion_map[unit_from]:
        result = conversion_map[unit_from][unit_to](value)
        label_result.config(
            text=f"{value} {unit_from} = {result:.4f} {unit_to}")
    else:
        label_result.config(text="Conversion not available.")


root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.config(bg="#f0f0f0")

label_value = tk.Label(root, text="Value:", bg="#f0f0f0")
label_value.pack(pady=5)
entry_value = tk.Entry(root, font=("Arial", 12))
entry_value.pack(pady=5)

label_from = tk.Label(root, text="Convert from:", bg="#f0f0f0")
label_from.pack(pady=5)
unit_from_var = tk.StringVar()
combo_from = ttk.Combobox(root, textvariable=unit_from_var,
                          font=("Arial", 12), state="readonly")
combo_from['values'] = list(conversion_map.keys())
combo_from.bind("<<ComboboxSelected>>", update_to_units)
combo_from.pack(pady=5)

label_to = tk.Label(root, text="Convert to:", bg="#f0f0f0")
label_to.pack(pady=5)
unit_to_var = tk.StringVar()
combo_to = ttk.Combobox(root, textvariable=unit_to_var,
                        font=("Arial", 12), state="readonly")
combo_to.pack(pady=5)

button_convert = tk.Button(root, text="Convert", command=convert, font=(
    "Arial", 12), bg="#4CAF50", fg="white")
button_convert.pack(pady=10)

label_result = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
label_result.pack(pady=5)

root.mainloop()
