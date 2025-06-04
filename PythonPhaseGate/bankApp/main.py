import function_bank
user_transaction = []
count = 0
while True:

    user_balance = int(input("enter user_balance: "))
    if user_balance < 100:
        user_transaction.append(user_balance)
        (print("Balance must be greater than N100."))

        continue
    print(f' your balance is {function_bank.create_account_for_user(user_balance)}')
    while True:
        #print(user_balance)
        withdrawal_amount = int(input("Enter amount to withdraw (multiples of 500 or 1000): "))
        if withdrawal_amount > user_balance:
                print("Insufficient funds. Please enter a valid amount.")
                continue
        elif withdrawal_amount % 500 != 0 and withdrawal_amount % 1000 != 0:
                print("Please enter an amount that is a multiple of 500 or 1000.")
                continue
        elif withdrawal_amount > 20000:
                print("The maximum amount you can withdraw at once is N20,000.")

        else:
            print(function_bank.user_transactions(withdrawal_amount, user_balance))
            to_continue = input('do you want to continue? ')
            to_continue= to_continue.lower()
            if to_continue == "yes":
                continue
            else:
                for details in user_transaction:
                  print(details)
                print(user_transaction)



