#
# print('Enter two integers, and I will tell you',
# 'the relationships they satisfy.')
#
# number1 = int(input('Enter first integer: '))
#
# number2 = int(input('Enter second integer: '))
# if number1 == number2:
# print(number1, 'is equal to', number2)
# if number1 != number2:
# print(number1, 'is not equal to', number2)
# if number1 < number2:
# print(number1, 'is less than', number2)
# if number1 > number2:
# print(number1, 'is greater than', number2)
# if number1 <= number2:
# print(number1, 'is less than or equal to', number2)
# if number1 >= number2:
# print(number1, 'is greater than or equal to', number2)


print('Enter two integers, and I will tell you',
'the relationships they satisfy.')
number1 = int(input('Enter first integer: '))

number2 = int(input('Enter second integer: '))

if number1 < number2 and number1 != number2:
    print(number1 , ' is lessthan or not equal to ', number2)
elif number1 == number2:
    print(number1, "is equal to ", number2)
else:
    print (number1, 'is greater than ', number2)
