largest = float('-inf')
second_largest = largest
for i in range(10):
    number = int(input('enter a number: '))
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print(largest)
print (second_largest)
