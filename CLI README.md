# Python Driving Academy 🚗

A command-line application for booking driving tests with customer management and employee access features.

## 📋 Project Overview

This Python application simulates a driving academy booking system where customers can book practical or theory tests, make payments, and receive receipts. Employees can access a database of all customer bookings through a secure login system.

## ✨ Features

### Customer Features
- **Test Booking Options:**
  - Practical Test (40 minutes) - £35
  - Practical Test (70 minutes) - £65
  - Theory Test (2 hours) - £23
- **Booking Management:** Enter personal details, preferred date/time
- **Payment Processing:** Secure card payment simulation
- **Receipt Generation:** Optional receipt printing with booking details

### Employee Features
- **Secure Login:** Username/password authentication
- **Database Access:** View all customer receipts and booking information
- **Customer Data:** Access to names, contact info, test details, and payment records

## 🛠️ How It Works

### Step 1: Welcome & User Selection
The application starts with a welcome message and asks users to identify themselves as either a customer or employee.

### Step 2: Customer Booking Flow
1. **Test Selection:** Choose between practical or theory tests
2. **Duration Choice:** For practical tests, select 40 or 70-minute sessions
3. **Personal Details:** Enter name, phone number, and address
4. **Scheduling:** Choose preferred date and time
5. **Payment:** Enter card details and confirm payment
6. **Receipt:** Option to print booking receipt

### Step 3: Employee Access
1. **Authentication:** Login with credentials (username: `sudo`, password: `sudomasterootuser`)
2. **Database View:** Access complete customer receipts database
3. **Information Display:** View all booking details including personal info and payment records

### Step 4: Data Storage
- Uses an in-memory dictionary (`receipts_db`) to store all booking information
- Each receipt gets a unique ID for tracking
- Card numbers are stored securely (last 4 digits only)

## 🔧 Technical Implementation

### Core Components
- **Menu System:** Interactive command-line interface
- **Data Management:** Dictionary-based storage system
- **Input Validation:** Basic error handling for user inputs
- **Security Features:** Password protection and card number masking

### Key Functions
- `display_welcome()` - Shows welcome message
- `customer_menu()` - Handles customer booking process
- `employee_menu()` - Manages employee login and database access
- `main()` - Controls application flow and user navigation

## 🚀 How to Run

1. **Prerequisites:** Python 3.x installed on your system
2. **Download:** Clone or download the `driving_academy.py` file
3. **Execute:** Run the following command in your terminal:
   ```bash
   python driving_academy.py
   ```
4. **Navigate:** Follow the on-screen prompts to book tests or access employee features

## 📊 Sample Usage

### Customer Booking Example
```
Welcome to Python Driving Academy

Are you a (1) Customer or (2) Employee? (3 to Exit)
Enter 1, 2, or 3: 1

Would you like to book a (1) Practical Test or (2) Theory Test?
Enter 1 or 2: 1

Practical Test Options:
1. 40 minutes - £35
2. 70 minutes - £65
Enter 1 or 2: 2

Enter your booking details:
Full Name: John Smith
Phone Number: 07123456789
Address: 123 Main St, London
...
```

### Employee Access Example
```
Employee Login
Username: sudo
Password: sudomasterootuser

Login successful! Accessing customer receipts database...
--- Customer Receipts Database ---
Receipt ID: 1
Name: John Smith
Test: Practical Test (70 minutes)
...
```

## 🔐 Security Features

- **Employee Authentication:** Protected login system
- **Data Privacy:** Card numbers stored with only last 4 digits
- **Access Control:** Customer and employee interfaces separated

## 📝 Future Enhancements

- [ ] Persistent data storage (database integration)
- [ ] Email receipt functionality
- [ ] Calendar integration for scheduling
- [ ] Multiple employee accounts
- [ ] Advanced payment processing
- [ ] Booking modification/cancellation features

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements or bug fixes!

---

*Created as a learning project to demonstrate Python programming concepts including user input handling, data management, and basic security implementation.*
