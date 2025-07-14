import tkinter as tk
from tkinter import messagebox, ttk
import datetime

# Dictionary to store customer receipts
receipts_db = {}

class DrivingAcademyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Driving Academy")
        self.root.geometry("600x400")
        self.root.configure(bg="#800080")  # Purple background

        # Welcome label
        self.welcome_label = tk.Label(
            root, 
            text="Welcome to Python Driving Academy", 
            font=("Arial", 20, "bold"), 
            fg="#FFA500",  # Orange text
            bg="#800080"
        )
        self.welcome_label.pack(pady=50)

        # Buttons
        self.customer_btn = tk.Button(
            root, 
            text="Customer", 
            command=self.open_customer_window, 
            font=("Arial", 14), 
            bg="#FFA500",  # Orange button
            fg="#800080",   # Purple text
            width=15
        )
        self.customer_btn.pack(pady=10)

        self.employee_btn = tk.Button(
            root, 
            text="Employee", 
            command=self.open_employee_window, 
            font=("Arial", 14), 
            bg="#FFA500", 
            fg="#800080", 
            width=15
        )
        self.employee_btn.pack(pady=10)

        self.exit_btn = tk.Button(
            root, 
            text="Exit", 
            command=self.root.quit, 
            font=("Arial", 14), 
            bg="#FFA500", 
            fg="#800080", 
            width=15
        )
        self.exit_btn.pack(pady=10)

    def open_customer_window(self):
        customer_window = tk.Toplevel(self.root)
        customer_window.title("Customer Booking")
        customer_window.geometry("500x600")
        customer_window.configure(bg="#800080")

        # Test type selection
        tk.Label(customer_window, text="Select Test Type", font=("Arial", 12), fg="#FFA500", bg="#800080").pack(pady=5)
        test_var = tk.StringVar(value="1")
        tk.Radiobutton(customer_window, text="Practical Test", variable=test_var, value="1", fg="#FFA500", bg="#800080", selectcolor="#800080").pack()
        tk.Radiobutton(customer_window, text="Theory Test", variable=test_var, value="2", fg="#FFA500", bg="#800080", selectcolor="#800080").pack()

        # Practical test duration (shown only when practical test is selected)
        duration_frame = tk.Frame(customer_window, bg="#800080")
        tk.Label(duration_frame, text="Practical Test Duration", font=("Arial", 12), fg="#FFA500", bg="#800080").pack(pady=5)
        duration_var = tk.StringVar(value="1")
        tk.Radiobutton(duration_frame, text="40 minutes - £35", variable=duration_var, value="1", fg="#FFA500", bg="#800080", selectcolor="#800080").pack()
        tk.Radiobutton(duration_frame, text="70 minutes - £65", variable=duration_var, value="2", fg="#FFA500", bg="#800080", selectcolor="#800080").pack()

        def update_duration_visibility():
            if test_var.get() == "1":
                duration_frame.pack(pady=10)
            else:
                duration_frame.pack_forget()

        test_var.trace("w", lambda *args: update_duration_visibility())
        update_duration_visibility()

        # Booking details
        tk.Label(customer_window, text="Booking Details", font=("Arial", 12, "bold"), fg="#FFA500", bg="#800080").pack(pady=10)
        
        tk.Label(customer_window, text="Full Name", fg="#FFA500", bg="#800080").pack()
        name_entry = tk.Entry(customer_window)
        name_entry.pack()

        tk.Label(customer_window, text="Phone Number", fg="#FFA500", bg="#800080").pack()
        phone_entry = tk.Entry(customer_window)
        phone_entry.pack()

        tk.Label(customer_window, text="Address", fg="#FFA500", bg="#800080").pack()
        address_entry = tk.Entry(customer_window)
        address_entry.pack()

        tk.Label(customer_window, text="Date (e.g., 30/06/2025)", fg="#FFA500", bg="#800080").pack()
        date_entry = tk.Entry(customer_window)
        date_entry.pack()

        tk.Label(customer_window, text="Time (e.g., 14:00)", fg="#FFA500", bg="#800080").pack()
        time_entry = tk.Entry(customer_window)
        time_entry.pack()

        tk.Label(customer_window, text="Card Number", fg="#FFA500", bg="#800080").pack()
        card_entry = tk.Entry(customer_window)
        card_entry.pack()

        def process_booking():
            if test_var.get() == "1":
                test_type = "Practical Test (40 minutes)" if duration_var.get() == "1" else "Practical Test (70 minutes)"
                price = 35 if duration_var.get() == "1" else 65
            else:
                test_type = "Theory Test (2 hours)"
                price = 23

            name = name_entry.get().strip()
            phone = phone_entry.get().strip()
            address = address_entry.get().strip()
            date = date_entry.get().strip()
            time = time_entry.get().strip()
            card_number = card_entry.get().strip()

            if not all([name, phone, address, date, time, card_number]):
                messagebox.showerror("Error", "All fields must be filled.")
                return

            confirm = messagebox.askyesno("Confirm Payment", f"Total to pay: £{price}\nConfirm payment?")
            if not confirm:
                messagebox.showinfo("Cancelled", "Payment cancelled. Booking not completed.")
                return

            receipt_id = len(receipts_db) + 1
            receipt = {
                "name": name,
                "phone": phone,
                "address": address,
                "test_type": test_type,
                "date": date,
                "time": time,
                "price": price,
                "card_number": card_number[-4:]
            }
            receipts_db[receipt_id] = receipt

            receipt_text = f"--- Receipt ---\nReceipt ID: {receipt_id}\nName: {name}\nTest: {test_type}\nDate: {date}\nTime: {time}\nAmount: £{price}"
            show_receipt = messagebox.askyesno("Receipt", "Booking successful! Would you like to view the receipt?")
            if show_receipt:
                messagebox.showinfo("Receipt", receipt_text)
            customer_window.destroy()

        tk.Button(
            customer_window, 
            text="Submit Booking", 
            command=process_booking, 
            font=("Arial", 12), 
            bg="#FFA500", 
            fg="#800080"
        ).pack(pady=20)

    def open_employee_window(self):
        employee_window = tk.Toplevel(self.root)
        employee_window.title("Employee Login")
        employee_window.geometry("400x300")
        employee_window.configure(bg="#800080")

        tk.Label(employee_window, text="Employee Login", font=("Arial", 16, "bold"), fg="#FFA500", bg="#800080").pack(pady=20)

        tk.Label(employee_window, text="Username", fg="#FFA500", bg="#800080").pack()
        username_entry = tk.Entry(employee_window)
        username_entry.pack()

        tk.Label(employee_window, text="Password", fg="#FFA500", bg="#800080").pack()
        password_entry = tk.Entry(employee_window, show="*")
        password_entry.pack()

        def check_login():
            username = username_entry.get().strip()
            password = password_entry.get().strip()

            if username == "sudo" and password == "sudomasterootuser":
                employee_window.destroy()
                self.show_receipts()
            else:
                messagebox.showerror("Error", "Invalid username or password.")

        tk.Button(
            employee_window, 
            text="Login", 
            command=check_login, 
            font=("Arial", 12), 
            bg="#FFA500", 
            fg="#800080"
        ).pack(pady=20)

    def show_receipts(self):
        receipts_window = tk.Toplevel(self.root)
        receipts_window.title("Customer Receipts Database")
        receipts_window.geometry("600x400")
        receipts_window.configure(bg="#800080")

        if not receipts_db:
            tk.Label(receipts_window, text="No receipts found.", font=("Arial", 12), fg="#FFA500", bg="#800080").pack(pady=20)
            return

        text_area = tk.Text(receipts_window, height=20, width=60, bg="#FFFFFF", fg="#800080")
        text_area.pack(pady=10)
        for receipt_id, receipt in receipts_db.items():
            text_area.insert(tk.END, f"Receipt ID: {receipt_id}\n")
            text_area.insert(tk.END, f"Name: {receipt['name']}\n")
            text_area.insert(tk.END, f"Phone: {receipt['phone']}\n")
            text_area.insert(tk.END, f"Address: {receipt['address']}\n")
            text_area.insert(tk.END, f"Test: {receipt['test_type']}\n")
            text_area.insert(tk.END, f"Date: {receipt['date']}\n")
            text_area.insert(tk.END, f"Time: {receipt['time']}\n")
            text_area.insert(tk.END, f"Amount: £{receipt['price']}\n")
            text_area.insert(tk.END, f"Card (last 4 digits): {receipt['card_number']}\n")
            text_area.insert(tk.END, "-------------------\n")
        text_area.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrivingAcademyApp(root)
    root.mainloop()