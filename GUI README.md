# Python Driving Academy Booking System

A Tkinter-based GUI application for managing driving test bookings at a fictional driving academy.

## Features

- Customer booking interface for theory and practical tests
- Employee login system to view all bookings
- Receipt generation and storage
- Payment processing simulation

## How It Works

### 1. Main Window
- Presents a welcome screen with three buttons:
  - Customer: Opens the booking interface
  - Employee: Opens the login portal
  - Exit: Closes the application

### 2. Customer Booking Process
1. **Test Type Selection**:
   - Choose between Practical Test or Theory Test
   - Practical test offers duration options (40min/70min) with different pricing

2. **Personal Details Collection**:
   - Full name, phone number, and address
   - Booking date and time
   - Payment card information (simulated)

3. **Booking Confirmation**:
   - Displays total price based on test selection
   - Asks for payment confirmation
   - Generates and stores a receipt
   - Offers to display the receipt

### 3. Employee Portal
- Secure login (username: `sudo`, password: `sudomasterootuser`)
- After successful login, displays all customer receipts with:
  - Booking details
  - Personal information
  - Payment information (last 4 digits of card)

## Technical Implementation

### Data Structure
- Uses a dictionary `receipts_db` to store all receipts with unique IDs

### GUI Elements
- Main window with purple background and orange accents
- Radio buttons for test selection
- Entry fields for customer information
- Text display area for receipts

### Validation
- Checks that all required fields are filled before processing
- Confirms payment before finalizing booking
