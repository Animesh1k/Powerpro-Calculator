import tkinter as tk
from tkinter import messagebox, Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Please  Select")
def cancel():
    root.destroy()
def unit():
    root.destroy()
    import unit_c
def temp():
    root.destroy()
    import temp_c

def back():
    root.destroy()
    import selection

def on_enter(event):
    but1.config(bg="crimson",fg="white")


def on_leave(event):
    but1.config(bg="SystemButtonFace",fg="black")

def on_enter1(event):
    but2.config(bg="green",fg="white")


def on_leave1(event):
    but2.config(bg="SystemButtonFace",fg="black")



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

background_image = Image.open("8152349_25196.jpg")
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)

background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

but1 =tk.Button(root,text="Unit Calculator ", command=unit,font=("Cascadia Mono SemiBold",12,"bold"),bd=5, width=26, height=1)
but1.grid(row=0, column=0, padx=15, pady=15)
but1.place(x=140,y=150)
but1.bind("<Enter>", on_enter)
but1.bind("<Leave>", on_leave)


but2 =tk.Button(root,text="Temperature Calculator",command=temp,font=("Cascadia Mono SemiBold",12,"bold"),bd=5, width=26, height=1)
but2.grid(row=0, column=0, padx=15, pady=15)
but2.place(x=140,y=220)
but2.bind("<Enter>", on_enter1)
but2.bind("<Leave>", on_leave1)




b_1 =tk.Button(root,text="Cancel", command=cancel,bg="red",fg="white",font=("Berlin Sans FB",15))
b_1.grid(row=0, column=0, padx=10, pady=10)
b_1.place(x=420,y=380)


b_2 =tk.Button(root,text="Back", command=back,bg="black",fg="white", font=("Berlin Sans FB",15))
b_2.grid(row=0, column=0, padx=10, pady=10)
b_2.place(x=10,y=380)



root.geometry("500x500")
root.resizable(False,False)

# Start the Tkinter main loop
root.mainloop()