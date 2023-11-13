import tkinter as tk
from tkinter import messagebox, Tk, Canvas, Entry, Text, Button, PhotoImage


# Function to validate the username and password

def on_enter3(event):
    cancel_button.config(bg="#FA0000",fg="white")


def on_leave3(event):
    cancel_button.config(bg="black",fg="white")

def on_enter2(event):
    login_button.config(bg="#04F649",fg="black")


def on_leave2(event):
    login_button.config(bg="blue",fg="white")
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace these with your actual username and password
    correct_username = "A"
    correct_password = "A"

    if username == correct_username and password == correct_password:
        root.destroy()
        import selection
        # messagebox.showinfo("Login Successful", "Welcome, " + username + "!")

    elif username == "" and password == "":
        messagebox.showinfo("Login Failed","Enter your Username and Password." )

    elif username == "":
        messagebox.showinfo("Login Failed","Enter your Username." )

    elif password == "":
        messagebox.showinfo("Login Failed","Enter your Password." )

    else:
        messagebox.showerror("Login Failed","Invalid username or password. Please try again.")


def cancel():
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("POWERPRO CALCULATOR")

# Customize colors
root.configure(bg="PeachPuff2")  # Set the background color of the window

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
    text="POWERPRO CALCULATOR",
    fill="#FFFFFF",
    font=("Copperplate Gothic Bold", 25 * -1)
)

# Create and place widgets on the window

username_label = tk.Label(root, text="Username :", font=("Copperplate Gothic Bold", 20))
username_label.pack(pady=10)
username_label.place(x=150, y=100)
username_entry = tk.Entry(root, bg="white", font=18,bd=4, background="#A5A5A5")
username_entry.pack(pady=5)
username_entry.place(x=150, y=150)

password_label = tk.Label(root, text="Password :", font=("Copperplate Gothic Bold", 20))
password_label.pack()
password_label.place(x=150, y=200)
password_entry = tk.Entry(root, show="*", bg="white", font=18,bd=4,background="#A5A5A5")
password_entry.pack(pady=10)
password_entry.place(x=150, y=250)

login_button = tk.Button(root, text="Login", command=validate_login, bg="blue", fg="white", font=("bold",18),bd=5,width=8,height=1)
login_button.pack()
login_button.place(x=70, y=380)
login_button.bind("<Enter>", on_enter2)
login_button.bind("<Leave>", on_leave2)

cancel_button = tk.Button(root, text="Cancel", command=cancel, bg="black", fg="white", font=("bold",18),bd=5,width=8,height=1)
cancel_button.pack()
cancel_button.place(y=380, x=300)
cancel_button.bind("<Enter>", on_enter3)
cancel_button.bind("<Leave>", on_leave3)

dev_label = tk.Label(root, text="© Developed By :",bg="peachpuff2" ,font=("Arial", 10,"bold","underline"))
dev_label.pack(pady=10)
dev_label.place(y=450, x=380)
dev_label = tk.Label(root, text="Animesh Khatua (TM)",bg="peachpuff2", font=("Arial", 7,"bold"))
dev_label.pack(pady=10)
dev_label.place(y=470, x=395)
dev_label = tk.Label(root, text="Ashutosh Das",bg="peachpuff2", font=("Arial", 7,"bold"))
dev_label.pack(pady=10)
dev_label.place(y=488, x=395)
dev_label = tk.Label(root, text="Gupteswar Achary" ,bg="peachpuff2", font=("Arial", 7,"bold"))
dev_label.pack(pady=10)
dev_label.place(y=505, x=395)

root.geometry("500x530")
root.resizable(False, False)

# Start the Tkinter main loop
root.mainloop()