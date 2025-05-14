number_of_student = int (input("Enter number of student"))
largest = 0
sutdentNumber = 0
for i in range(number_of_student):
   score = int(input(f"Enter score for student: {i + 1} :"))
   if score > largest:
       largest = score
       sutdentNumber = i

print(f'the highest score is student:{sutdentNumber + 1} with:  {largest}')
