userAmount = int((input("enter Amount: ")))
while userAmount < 1000:
   userAmount = int((input(" wrong input, enter Amount greater than 1000: ")))
if userAmount >= 1000 and userAmount <= 10000:
    discounted = userAmount *  0.05
    print(f"your  discounted fee is:{userAmount *  0.05} ")
    print(f"your amount to be paid is :{userAmount - discounted:,.2f}")
elif userAmount > 10000 and userAmount <= 50000:
    discounted = userAmount *  0.1
    print(f"your  discounted fee is:{userAmount *  0.1} ")
    print(f"your amount to be paid is {userAmount - discounted:,.2f}")
elif userAmount > 50000:
    discounted = userAmount *  0.2
    print(f"your  discounted fee is:{userAmount *  0.2} ")
    print(f"your amount to be paid is {userAmount - discounted:,.2f}")





