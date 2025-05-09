# a=b=7
# print('a =', a, '\nb =', b)

# for row in range(10):
#     for column in range(10):
#             print('<' if row % 2 == 1 else '>', end=' ')
#     print()

# for row in range(2):
#     for colume in range(7):
#         print('@', end='')
#     print()






# # Printing the header
# print(f"{'Number':>6} {'Square':>6} {'Cube':>6}")
#
# # Printing each row manually
# print(f"{0:>6} {0**2:>6} {0**3:>6}")
# print(f"{1:>6} {1**2:>6} {1**3:>6}")
# print(f"{2:>6} {2**2:>6} {2**3:>6}")
# print(f"{3:>6} {3**2:>6} {3**3:>6}")
# print(f"{4:>6} {4**2:>6} {4**3:>6}")
# print(f"{5:>6} {5**2:>6} {5**3:>6}")

# # Printing the header
# print("Number\tSquare\tCube")
#
# # Printing each row manually
# print(f"{0}\t{0**2}\t{0**3}")
# print(f"{1}\t{1**2}\t{1**3}")
# print(f"{2}\t{2**2}\t{2**3}")
# print(f"{3}\t{3**2}\t{3**3}")
# print(f"{4}\t{4**2}\t{4**3}")
# print(f"{5}\t{5**2}\t{5**3}")

# averageTotal = 0
# count = 0
# while True:
#     gallonsUsed = float(input ('enter gallons used (enter -1 to stop): '))
#     if gallonsUsed == -1:
#         break
#     miles = int(input('Enter the miles driven: '))
#     total = miles / gallonsUsed
#     averageTotal += total
#     print(f'The miles/gallon for this tank was {total}')
#     count += 1
#
# print(f'The overall average miles/gallon was{averageTotal / count}')










# userinput = int (input("enter a number: "))
# largest = userinput
# second_largest = userinput
# count = 9
# while count >= 1:
#     secondInput =  int (input("enter a number: "))
#     if secondInput > largest:
#         second_largest = largest
#         largest = secondInput
#     elif secondInput > second_largest and secondInput != largest:
#         second_largest = secondInput
#     count = count -1
#
# print(f'the largest is {largest}')
# print(f'the  second largest is {second_largest}')


input = a, b= 5,10
print(a,b , end=',')

