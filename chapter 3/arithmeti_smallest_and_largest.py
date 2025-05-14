
smallest = float('inf')
largest = 0
product = 1
average = 0
sum = 0

for number in range(1,5):
    number = int(input("enter interger: "))
    sum += number
    product *= number
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

average = float(sum) / 4
print (f'the smallest is {smallest}')
print (f'the largest is {largest}')
print (f'the produst of all numbers  is {product}')
print (f'the sum of all numbers is {sum}')
print (f'the average of the numbers  is {average}')


