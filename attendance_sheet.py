import tkinter as tk
from tkinter import messagebox, PhotoImage
import subprocess
from PIL import Image, ImageTk
# Function to calculate attendance percentage
def calculate_percentage():
    try:
        attendance_data = [int(attendance_entries[i].get()) for i in range(15)]
        present_days = sum(attendance_data)
        total_days = len(attendance_data)
        attendance_percentage = (present_days / total_days) * 100
        result_label.config(text=f"Attendance Percentage: {attendance_percentage:.2f}%", fg="green")
    except ValueError:
        result_label.config(text="Error: Please Enter all the values", fg="red")

def cancel():
    app.destroy()
def back():
    subprocess.Popen(["python", "selection.py"])
    app.destroy()

# Function to validate input (allow only 0 and 1)
def validate_input(P):
    if P in ('', '0', '1'):
        return True
    else:
        messagebox.showerror("Invalid Input", "Please enter only 0 or 1.")
        return False

# Create the main application window
app = tk.Tk()
app.title("Student Attendance Calculator")

# To set background image
background_image = Image.open("pexels-pixabay-235985.jpg")
window_width = app.winfo_screenwidth()
window_height = app.winfo_screenheight()
background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)

background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Create and configure labels, entry fields, and buttons
instruction_label = tk.Label(app, text="Enter attendance for the last 15 days:", font=("Arial", 12,"bold") , bg="crimson", fg="white" ,height=2,width=100)
instruction_label.pack(pady=10)
app.configure(bg="#91F99D")


attendance_entries = [tk.Entry(app, width=5, validate="key", validatecommand=(app.register(validate_input), "%P")) for _ in range(15)]

for day in range(1, 16):
    day_label = tk.Label(app, text=f"Day {day}:",bg="bisque2" ,font=("Arial", 10))
    day_label.pack()
    attendance_entries[day-1].pack()



calculate_button = tk.Button(app, text="Calculate Percentage", command=calculate_percentage, bg="blue", fg="white")
calculate_button.pack(pady=10)

but1 =tk.Button(app,text="Cancel", command=cancel,bg="red",fg="white",font=("Berlin Sans FB",15))
but1.place(x=215,y=750)


but2 =tk.Button(app,text="Back", command=back,bg="black",fg="white", font=("Berlin Sans FB",15))
but2.place(x=10,y=750)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack()


app.geometry("300x800")
app.resizable(False,False)
# Run the Tkinter main loop
app.mainloop()