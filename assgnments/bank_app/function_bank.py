import random
def generate_random_account_number():
     return random.randint(1000000000, 9999999999)

def open_account(name, bal=0.0):
    if bal < 0:
        raise ValueError("Balance cannot be negative.")
    accountNumber = generate_random_account_number()
    user_account=[name, accountNumber, bal]
    return user_account

def deposit(account, amount):
    if isinstance(amount, str) and (not amount.strip()):
        raise ValueError("Amount cannot be empty or just spaces.")
    float(amount)
    if amount<= 0:
        raise ValueError("Amount cannot be less or equal to zero")
    account[2]+=amount
    return account[2]

def withdral_amount(account, amount):
    if isinstance(amount, str) and (not amount.strip()):
        raise ValueError("Amount cannot be empty or just spaces.")
    float(amount)
    if amount<= 0:
        raise ValueError("Amount cannot be less or equal to zero")
    account[2]-=amount
    return account[2]
