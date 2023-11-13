import tkinter as tk
from tkinter import messagebox, Tk, Canvas, Entry, Text, Button, PhotoImage

root = tk.Tk()
root.title("Please  Select")
def cancel():
    root.destroy()

def income():
    root.destroy()
    import income_expense

def elec():
    root.destroy()
    import electricity

def scale():
    root.destroy()
    import scale_selection

def attendance():
    root.destroy()
    import attendance_sheet
def back():
    root.destroy()
    import powerpro_calc

def on_enter(event):
    but1.config(bg="lightblue")


def on_leave(event):
    but1.config(bg="SystemButtonFace")

def on_enter1(event):
    but2.config(bg="pink")


def on_leave1(event):
    but2.config(bg="SystemButtonFace")

def on_enter2(event):
    but3.config(bg="#91F99D")


def on_leave2(event):
    but3.config(bg="SystemButtonFace")

def on_enter3(event):
    but4.config(bg="#9E8FFB")


def on_leave3(event):
    but4.config(bg="SystemButtonFace")
# Customize colors
root.configure(bg="PeachPuff2")

canvas = Canvas(
    root,
    bg="#FFFFFF",
    height=350,
    width=610,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    610.0,
    89.0,
    fill="#BB3838",
    outline="")

canvas.create_text(
    85.0,
    25.0,
    anchor="nw",
    text="SELECT YOUR CHOICE",
    fill="#FFFFFF",
    font=("Copperplate Gothic Bold", 25 * -1)
)


but1 =tk.Button(root,text="Income Expense Calculator ", command=income,font=("Cascadia Mono SemiBold",10,"bold"),bd=5, width=26, height=1)
but1.grid(row=0, column=0, padx=15, pady=15)
but1.place(x=140,y=100)
but1.bind("<Enter>", on_enter)
but1.bind("<Leave>", on_leave)


but2 =tk.Button(root,text="Converter Calculation",command=scale,font=("Cascadia Mono SemiBold",10,"bold"),bd=5, width=26, height=1)
but2.grid(row=0, column=0, padx=15, pady=15)
but2.place(x=140,y=160)
but2.bind("<Enter>", on_enter1)
but2.bind("<Leave>", on_leave1)

but3 =tk.Button(root,text="Attendance Calculation", command=attendance, font=("Cascadia Mono SemiBold",10,"bold"),bd=5, width=26, height=1)
but3.grid(row=10, column=10, padx=15, pady=15)
but3.place(x=140,y=220)
but3.bind("<Enter>", on_enter2)
but3.bind("<Leave>", on_leave2)

but4 =tk.Button(root,text="Electricity Calculation",command=elec ,font=("Cascadia Mono SemiBold",10,"bold"),bd=5, width=26, height=1)
but4.grid(row=0, column=0, padx=15, pady=15)
but4.place(x=140,y=280)
but4.bind("<Enter>", on_enter3)
but4.bind("<Leave>", on_leave3)


b_1 =tk.Button(root,text="Cancel", command=cancel,bg="red",fg="white",font=("Berlin Sans FB",15))
b_1.grid(row=0, column=0, padx=10, pady=10)
b_1.place(x=420,y=400)


b_2 =tk.Button(root,text="Back", command=back,bg="black",fg="white", font=("Berlin Sans FB",15))
b_2.grid(row=0, column=0, padx=10, pady=10)
b_2.place(x=10,y=400)



root.geometry("500x500")
root.resizable(False,False)

# Start the Tkinter main loop
root.mainloop()