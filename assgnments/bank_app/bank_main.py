import function_bank

# # user_name = input('enter your name: ')
account = function_bank.open_account("John Doe", 500)
print(f"Account created: {account}")
new_balance = function_bank.deposit(account, 500)
print(f"Deposited 200. New balance: {new_balance}")
remove_balance = function_bank.withdral_amount(account, 200)
print(f"withdrew 200. New balance: {remove_balance}")
print(account)
