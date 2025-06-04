#enter their account balance to start
#withdral money{
#1- must be multiples of 500,1000 only
#2-fix withral of 100
#3-user cannot withdral 90% of their total
#4-the remaining balance must be 100
#}
# display acc details after each withdral
#show account withdrawn, withdral fee, remaining balance
#if withdral amount are not met prompt the user to enter a valid amount
#allow multiple withdral until user choose to exit
#user should be able to log and see their transction


userAccount = 0;
user_transction = []

while True:
   userInput = int(input('Enter your account balance: '))
   if userInput <= 100:
       print("user account cannot be a negative number or less than 100")
       continue

   #userAccount.append(userInput);
   userAccount = userInput
   print(f'your account balance is N{userAccount}')

   while True:
        withdral_amount = int(input("enter amount to withdral, multiples of 500 or 1000 "))
        if withdral_amount % 500 != 0 and withdral_amount % 1000 != 0:
             print("kindly enter anamunt that is mulitple of 500 and 100")

        # elif userAccount == 100:
        #     print("your Balance is N100, sorry yo cnnot perform any other action")

        elif withdral_amount > userAccount:
            print("amount greater than user account, kindly enter a valid amount")
            continue
        elif withdral_amount > 20000:
            print("the least amount you can withdra per time is N20000")

        else:
            userAccount = userAccount - (withdral_amount + 100)
            print('Transction successful')
            print(f'withdral amount is: N{withdral_amount}')
            print(f'withdral fee is: N100')
            print(f'Remaining Balance is: N{userAccount}')

            question = input("you you want to withdral another amount? yes or no")
            question = question.lower()
            if question == 'yes':
                continue
            elif question == 'no':
                break
            else:
                print('enter a valid input')


 user_transactions.append({
                    "type": "Withdrawal",
                    "amount": withdrawal_amount,
                    "fee": 100,
                    "success": True,
                    "remaining_balance": user_account
                })

  print("\nTransaction History:")
            for idx, txn in enumerate(user_transactions, 1):
                status = "Success" if txn["success"] else "Failed"
                print(f"{idx}. {txn['type']} of N{txn['amount']} | Fee: N{txn['fee']} | Status: {status} | Remaining Balance: N{txn['remaining_balance']}")



