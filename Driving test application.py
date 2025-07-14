# Import required modules
import datetime

# Dictionary to store customer receipts (acting as a simple database)
receipts_db = {}

# Function to display the welcome message
def display_welcome():
    print("Welcome to Python Driving Academy")

# Function to handle customer booking process
def customer_menu():
    print("\nWould you like to book a (1) Practical Test or (2) Theory Test?")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        print("\nPractical Test Options:")
        print("1. 40 minutes - £35")
        print("2. 70 minutes - £65")
        duration_choice = input("Enter 1 or 2: ").strip()
        
        if duration_choice == "1":
            test_type = "Practical Test (40 minutes)"
            price = 35
        elif duration_choice == "2":
            test_type = "Practical Test (70 minutes)"
            price = 65
        else:
            print("Invalid choice. Returning to main menu.")
            return
    elif choice == "2":
        test_type = "Theory Test (2 hours)"
        price = 23
    else:
        print("Invalid choice. Returning to main menu.")
        return
    
    # Get booking details
    print("\nEnter your booking details:")
    name = input("Full Name: ").strip()
    phone = input("Phone Number: ").strip()
    address = input("Address: ").strip()
    
    # Get date and time for booking
    print("\nAvailable every day, any time. Enter your preferred date and time.")
    date = input("Date (e.g., 30/06/2025): ").strip()
    time = input("Time (e.g., 14:00): ").strip()
    
    # Payment details
    print("\nPayment Details")
    card_number = input("Card Number: ").strip()
    print(f"\nTotal to pay: £{price}")
    confirm_payment = input("Confirm payment (yes/no)? ").strip().lower()
    
    if confirm_payment != "yes":
        print("Payment cancelled. Booking not completed.")
        return
    
    # Generate receipt
    receipt_id = len(receipts_db) + 1
    receipt = {
        "name": name,
        "phone": phone,
        "address": address,
        "test_type": test_type,
        "date": date,
        "time": time,
        "price": price,
        "card_number": card_number[-4:]  # Store last 4 digits for security
    }
    receipts_db[receipt_id] = receipt
    
    print("\nThank you for your purchase with Python Driving Academy!")
    receipt_choice = input("Would you like a receipt (yes/no)? ").strip().lower()
    
    if receipt_choice == "yes":
        print("\n--- Receipt ---")
        print(f"Receipt ID: {receipt_id}")
        print(f"Name: {name}")
        print(f"Test: {test_type}")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print(f"Amount: £{price}")
        print("---------------")

# Function to handle employee login and database access
def employee_menu():
    print("\nEmployee Login")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    # Check credentials
    if username == "sudo" and password == "sudomasterootuser":
        print("\nLogin successful! Accessing customer receipts database...")
        if not receipts_db:
            print("No receipts found.")
        else:
            print("\n--- Customer Receipts Database ---")
            for receipt_id, receipt in receipts_db.items():
                print(f"Receipt ID: {receipt_id}")
                print(f"Name: {receipt['name']}")
                print(f"Phone: {receipt['phone']}")
                print(f"Address: {receipt['address']}")
                print(f"Test: {receipt['test_type']}")
                print(f"Date: {receipt['date']}")
                print(f"Time: {receipt['time']}")
                print(f"Amount: £{receipt['price']}")
                print(f"Card (last 4 digits): {receipt['card_number']}")
                print("-------------------")
    else:
        print("Invalid username or password.")

# Main function to run the application
def main():
    display_welcome()
    while True:
        print("\nAre you a (1) Customer or (2) Employee? (3 to Exit)")
        user_type = input("Enter 1, 2, or 3: ").strip()
        
        if user_type == "1":
            customer_menu()
        elif user_type == "2":
            employee_menu()
        elif user_type == "3":
            print("Thank you for using Python Driving Academy. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the application
if __name__ == "__main__":
    main()