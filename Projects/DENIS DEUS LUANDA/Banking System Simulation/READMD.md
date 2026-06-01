# Banking System Console Application

## Overview

The Banking System Simulation Console Application is a Python-based program developed using Object-Oriented Programming (OOP) principles. The application simulates basic banking operations such as account creation, deposits, withdrawals, and balance inquiries through a command-line interface.

The project demonstrates the use of classes, objects, constructors, methods, encapsulation, loops, conditional statements, and exception handling.

## Features

* Create a bank account
* Deposit money
* Withdraw money
* Check account balance
* Prevent overdrawing
* Validate user input
* Menu-driven interface

## Technologies Used

* Python 3
* VS code
* Object-Oriented Programming (OOP)

## Program Structure

```text
BankAccount Class
│
├── __init__()
├── deposit()
├── withdraw()
└── check_balance()

Main Program
│
├── Create Account
├── Display Menu
├── Deposit
├── Withdraw
├── Check Balance
└── Exit
```

## OOP Concepts Implemented

### Class

The program uses a `BankAccount` class as a blueprint for creating bank account objects.

### Object

A bank account object is created from the `BankAccount` class.

### Constructor

The constructor (`__init__`) initializes account details such as account holder name, account number, and balance.

### Encapsulation

The account balance is stored in a private variable:

```python
self.__balance
```

This prevents direct access and modification from outside the class.

### Methods

* `deposit()` – Adds funds to the account.
* `withdraw()` – Removes funds from the account.
* `check_balance()` – Displays the current account balance.

## How to Run

1. Install Python 3.
2. Save the source code as `banking_system.py`.
3. Open Terminal or Command Prompt.
4. Navigate to the project directory.
5. Execute:

```bash
python banking_system.py
```

## Sample Output

```text
Enter account holder name: Denis
Enter account number: 1001

===== BANKING SYSTEM =====
1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Enter your choice: 1
Enter deposit amount: 10000

Deposited: 10000.0. New balance: 10000.0
```

## Future Improvements

* Transaction history
* Multiple account support
* Database integration
* Graphical User Interface (GUI)
* User authentication system

## Author

Developed as an Object-Oriented Programming Banking System Simulation Assignment using Python.
