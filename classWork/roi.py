investAmount = int(input("enter invest amount: "))
numberOfYears = int(input("enter number of years: "))
InterestRate = int(input("enter interest rate: "))

rate = InterestRate / 100


for i in range (1, numberOfYears +1):
    compountInterest = investAmount * ( 1+ rate) **i
    print(f'your interest  for year{i} is ${compountInterest:,.2f}')

