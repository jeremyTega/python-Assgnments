userInput = int(input("enter a number: "))

while userInput < 1:
    userInput = int(input("enter a number: "))
      if userInput > 1:
         for i in range(userInput, 1, -1):
        print(i)
        if i == 1:
            print("BLAST OFF")
