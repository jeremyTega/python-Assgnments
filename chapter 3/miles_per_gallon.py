averageTotal = 0
count = 0
while True:
    gallonsUsed = float(input ('enter gallons used (enter -1 to stop): '))
    if gallonsUsed == -1:
        break
    miles = int(input('Enter the miles driven: '))
    total = miles / gallonsUsed
    averageTotal += total
    print(f'The miles/gallon for this tank was {total}')
    count += 1

print(f'The overall average miles/gallon was{averageTotal / count}')
