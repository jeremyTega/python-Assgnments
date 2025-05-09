userinput = int(input("enter a number"))
factoria = 1
if userinput < 1:
    print("enter a positive number")
elif userinput > 1:
    for i in range(userinput, 0, -1):
        #print(i)
        factoria = factoria * i
print(f'the factoria of {userinput} is {factoria}')
