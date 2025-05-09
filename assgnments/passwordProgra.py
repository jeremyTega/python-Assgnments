userInput = input('enter your password')
length = 0;
for i in (userInput):
   # print(i)
    length +=1
    #print(length)

if length < 8:
     print("passwprd very weak")
elif length == 8:
     print("password is weak")
elif length > 8 and  length <= 16 :
     print("password is strong")
elif length  > 16:
    print("password is very strong")
