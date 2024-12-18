# Task 1: Develop an Advanced Bank Account Management System

## Description
As a user, I want an advanced bank account management system that allows me to create and manage multiple bank accounts, perform transactions, and view account summaries so that I can handle my financial operations efficiently.

## Acceptance Criteria

### Account Creation
- A user can create a new bank account with the following attributes:
  - **Account Number**: A unique identifier for the account.
  - **Initial Balance**: The starting balance for the account (default is 0).
- The system must confirm the successful creation of an account.

### Deposits
- A user can deposit money into a specified account.
- The deposit amount must be a positive number.
- The system must update the account balance accordingly and confirm the transaction.

### Withdrawals
- A user can withdraw money from a specified account.
- The withdrawal amount must be:
  - Greater than 0.
  - Less than or equal to the current balance.
- The system must update the account balance accordingly and confirm the transaction.

### Account Summary
- A user can view a list of all accounts with their account numbers and current balances.

### Money Transfers
- A user can transfer money between two accounts.
- The source account must have sufficient balance for the transfer.
- The system must confirm successful transfers by updating the balances of both accounts.

## Technical Notes
- Use a `BankAccount` class to represent individual accounts.
- Use an `AccountManager` class to manage multiple accounts and transactions.
- Ensure that transaction methods include appropriate validation for deposits, withdrawals, and transfers.


# Task 2: Develop a To-Do List Application for Task Management

## Description
As a user, I want a To-Do List application that allows me to create and manage tasks so that I can stay organized and prioritize my workload effectively.

## Class diagram 
![Снимок экрана 2024-12-18 191729](https://github.com/user-attachments/assets/417fa3e7-3358-4e96-a1c9-8cd407f7bde2)
