# Bank Account System

A small object-oriented banking program in Python that models a customer account with deposits, withdrawals and balance checks.

## Concepts covered

- **Classes and objects:** `PersonalDetails` stores the account holder, and `BankDetails` manages the money
- **Inheritance:** `BankDetails` extends `PersonalDetails` and calls `super().__init__()`
- **Input validation:** rejects zero or negative amounts, and withdrawals larger than the balance

## Run it

```bash
python bank_account.py
```

You'll be asked for a name and password. The script then runs a sample set of deposits and a withdrawal and prints the balance after each one.

## Example output

```
Enter name: Namay
Enter password: ****
Deposit successful. New balance: 2000
Deposit successful. New balance: 7000
Withdraw successful. New balance: 4000
```

## Ideas for next steps

- Hash the password instead of storing plain text
- Add a menu loop so the user picks deposit / withdraw / balance
- Save accounts to a file or SQLite database

## License

MIT
