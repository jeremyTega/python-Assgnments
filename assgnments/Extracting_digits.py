entered_number = int(input("enter an interger from 1 - 10,000: "))
sum = 0;
if 1 <= entered_number <= 10000:
    while  entered_number > 0:
       extract_one = entered_number  % 10
       sum +=extract_one
       entered_number = entered_number // 10

    print(f'the sum of all numbers entered is: {sum}')

else:
    print("not a valid number")

