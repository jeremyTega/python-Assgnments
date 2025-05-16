entered_number = int(input("enter an interger from 1 - 10,000: "))

def sum_number(entered_number):
    sum = 0
    while  entered_number > 0:
       extract_one = entered_number  % 10
       sum +=extract_one
       entered_number = entered_number // 10
    return f'the sum is {sum}'



if 1 <= entered_number <= 10000:
   print(sum_number(entered_number))
else:
    print("not a valid number")
