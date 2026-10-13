# 🏦 OOP Banking Application

A command-line interface (CLI) banking management system built with **Python**, designed to demonstrate core **Object-Oriented Programming (OOP)** concepts. The application simulates real-world banking workflows, including user authentication, account creation, and distinct behaviors for Savings and Current accounts—including dynamic overdraft limits.

---

## ✨ Features

- **User Authentication & Account Setup**:
  - Open new **Savings** or **Current** accounts.
  - Auto-incrementing account number generation.
  - Login system using user credentials (Name & Aadhaar Number).

- **Savings Account**:
  - Real-time balance inquiry.
  - Funds deposit.
  - Standard withdrawal with balance checks.

- **Current Account**:
  - Real-time balance inquiry.
  - Funds deposit with lifetime highest balance tracking.
  - **Dynamic Overdraft (OD) Limit**: Automatically updates OD limit to 25% of the highest recorded balance.
  - Overdraft-assisted withdrawals.

- **Object-Oriented Design**:
  - **Abstraction**: Uses Python’s `abc` module (`ABC`, `@abstractmethod`) to enforce interface consistency.
  - **Inheritance & Multiple Inheritance**: Inherits structural data from `Database` and contract methods from `requirements`.
  - **Encapsulation**: Encapsulates user credentials using private class attributes (`__user_credentials`).

---

## 🛠️ System Architecture

```text
Database (Data Store)          requirements (Abstract Base Class)
     │                                    │
     └──────────────┬─────────────────────┘
                    │
            ┌───────┴───────┐
            │               │
         Saving        Current_Acc
            │               │
            └───────┬───────┘
                    │
                   Bank (Main Controller & CLI Menu)
