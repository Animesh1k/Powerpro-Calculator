import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, PhotoImage
import subprocess
from PIL import Image, ImageTk

def cancel():
    app.destroy()


def back():
    subprocess.Popen(["python", "scale_selection.py"])
    app.destroy()

def on_enter(event):
    calculate_button.config(bg="green")


def on_leave(event):
    calculate_button.config(bg="blue")
def convert():
    try:
        input_value = float(power_entry.get())
        selected_unit = unit_combobox.get()
        result_label.config(text="")

        if selected_unit == "Fahrenheit to Celsius":
            # result = input_value / 1000
            result = (input_value - 32) * 5 / 9

        elif selected_unit == "Celsius to Fahrenheit":
            # result = input_value * 1000
            result = (input_value * 9 / 5) + 32
        else:
            result_label.config(text="Invalid conversion")
            return

        result_label.config(text=f"Result: {result:.2f} {selected_unit.split()[-1]}",font="bold")
    except ValueError:
        result_label.config(text="Warning! Please enter a number.",font="bold")


# Create the main application window
app = tk.Tk()
app.title("Electricity Calculator")
app.config(bg="#9E8FFB")

background_image = Image.open("blue-circles-different-sizes-seamless-yellow-pattern.jpg")
window_width = app.winfo_screenwidth()
window_height = app.winfo_screenheight()
background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)

background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and configure input labels and entry widgets
power_label = tk.Label(app, text="Enter a value to convert:",bd=6,font=("Cascadia Code SemiBold",12))
power_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
power_entry = tk.Entry(app,bd=4,font=10)
power_entry.grid(row=0, column=1, padx=10, pady=5)

unit_combobox = ttk.Combobox(app, values=["Fahrenheit to Celsius", "Celsius to Fahrenheit"],font=10)
unit_combobox.grid(row=1, column=0, padx=5, pady=5)
unit_combobox.set("Fahrenheit to Celsius")
unit_combobox.place(x=130, y=100)

# Create and configure the calculate button
calculate_button = tk.Button(app, text="Calculate", command=convert, bg="blue", fg="white", font=("Arial", 14, "bold"))
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
calculate_button.place(x=200, y=180)
calculate_button.bind("<Enter>", on_enter)
calculate_button.bind("<Leave>", on_leave)

but2 = tk.Button(app, text="Back", bg="black", fg="white", command=back, font=("Berlin Sans FB", 15))
but2.place(x=10, y=250)

but1 = tk.Button(app, text="Cancel", command=cancel, bg="red", fg="white", font=("Berlin Sans FB", 15))
but1.place(x=446, y=250)

# Create and configure the result label
result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=5)

app.geometry("530x300")
app.resizable(False, False)
# Start the GUI event loop
app.mainloop()