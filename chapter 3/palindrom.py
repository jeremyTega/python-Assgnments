userNumber = int(input('Enter a five-digit number: '))

if userNumber < 10000 or userNumber > 99999:
    print("Please enter a 5-digit number.")
else:
    myNumber = userNumber
    reversedNumber = 0

    while myNumber > 0:
        digit = myNumber % 10
        reversedNumber = reversedNumber * 10 + digit
        myNumber //= 10

    if userNumber == reversedNumber:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
