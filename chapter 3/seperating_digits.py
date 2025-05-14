user_digits = int(input('enter 5 digit number'))

if 10000 <= user_digits <= 99999:
    for i in (4,-1,-1):
        digit = (user_digits // (10 ** i)) % 10
        print(digit)

