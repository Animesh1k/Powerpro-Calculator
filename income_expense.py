import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
def cancel():
    app.destroy()
def back():
    subprocess.Popen(["python", "selection.py"])
    app.destroy()

# Function to calculate remaining balance
def calculate_balance():
    try:
        # Get income and expense for each day from input fields
        income = [float(income_entries[i].get()) for i in range(6)]
        expense = [float(expense_entries[i].get()) for i in range(6)]

        # Calculate total income and total expense
        total_income = sum(income)
        total_expense = sum(expense)

        # Check if expense is greater than income for any day
        if any(expense[i] > income[i] for i in range(6)):
            messagebox.showerror("Error", "Expense should not be greater than income for any day.")
            return
        remaining_balance = total_income - total_expense

        # Display the result
        result_label.config(text=f"Remaining Balance: Rs.{remaining_balance:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter all values for income and expense.")


# Create the main application window
app = tk.Tk()
app.title("Income and Expense Calculator")
app.geometry("500x400")
app.configure(bg="lightblue")
background_image = Image.open("pexels-nataliya-vaitkevich-6863530.jpg")
window_width = app.winfo_screenwidth()
window_height = app.winfo_screenheight()
background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)

background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Labels, Entry fields, and Checkboxes for each day of the week
days = ["First Day", "Second day", "Third day", "Fourth day", "Fifth day", "Sixth day", "Last day"]
income_labels = []
income_entries = []
expense_labels = []
expense_entries = []



for i, day in enumerate(days):
    income_label = tk.Label(app, text=f"{day} Income:")
    income_entry = tk.Entry(app)
    expense_label = tk.Label(app, text=f"{day} Expense:")
    expense_entry = tk.Entry(app)



    income_labels.append(income_label)
    income_entries.append(income_entry)
    expense_labels.append(expense_label)
    expense_entries.append(expense_entry)

    income_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    income_entry.grid(row=i, column=1, padx=10, pady=5)
    expense_label.grid(row=i, column=2, padx=10, pady=5, sticky="w")
    expense_entry.grid(row=i, column=3, padx=10, pady=5)


# Calculate button
calculate_button = tk.Button(app, text="Calculate Balance", command=calculate_balance,bg="#3333ff",fg="white")

but1 =tk.Button(app,text="Cancel", command=cancel,bg="red",fg="white",font=("Berlin Sans FB",15))
but1.place(x=515,y=450)


but2 =tk.Button(app,text="Back",bg="black",fg="white", command=back, font=("Berlin Sans FB",15))
but2.place(x=10,y=450)

# Result label
result_label = tk.Label(app, text="Remaining Balance:")

# Place widgets on the window
calculate_button.grid(row=7, column=0, columnspan=4, pady=10)
result_label.grid(row=8, column=0, columnspan=4, pady=10)

app.geometry("600x500")
app.resizable(False,False)
# Start the GUI application
app.mainloop()