import tkinter as tk
from tkinter import messagebox, PhotoImage
import subprocess
from PIL import Image, ImageTk

def cancel():
    root.destroy()
def back():
    subprocess.Popen(["python", "selection.py"])
    root.destroy()
def calculate_cost():
    try:
        units = float(entry_units.get())
        if units <= 0:
            result_label.config(text="Power Consumption Should be positive.")
        else:
            if units <= 50:
                cost = units * 6
            else:
                cost = 50 * 6 + (units - 50) * 6.5
            result_label.config(text=f"Total Electricity Bill Amount: Rs.{cost:.2f}",font=("Cascadia Mono SemiBold",12))
    except ValueError:
        result_label.config(text="Error:Enter the Electricity Consumption!",font=("Cascadia Mono SemiBold",12))

# Create the main application window
root = tk.Tk()
root.title("Electricity Cost Calculator")

background_image = Image.open("4312588_6454.jpg")
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)

background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label and entry for entering units
units_label = tk.Label(root, text="Enter Units Consumed :",bd=6,height=1,width=30,font=("Berlin Sans FB",15))
units_label.pack(pady=10)
entry_units = tk.Entry(root,font=10)
entry_units.pack()



# Create a button to calculate the cost
calculate_button = tk.Button(root, text="Calculate Cost", command=calculate_cost,bg="blue",fg="white",font=("bold",12),bd=5)
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

but2 = tk.Button(root, text="Back", bg="black", fg="white", command=back, font=("Berlin Sans FB", 15))
but2.place(x=10, y=250)

but1 = tk.Button(root, text="Cancel", command=cancel, bg="red", fg="white", font=("Berlin Sans FB", 15))
but1.place(x=417, y=250)

root.geometry("500x350")
root.resizable(False,False)
# Start the GUI event loop
root.mainloop()
