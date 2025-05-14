number_of_student = int (input("Enter number of student"))
largest = 0
second_largest = 0
first_student_number = 0
second_student_number =0

for i in range(number_of_student):
        score = int(input(f"Enter score for student {i + 1}: "))
        if score > largest:
            second_largest = largest
            second_student_number = first_student_number
            largest = score
            first_student_number = i
        elif score > second_largest and score != largest:
            second_largest = score
            second_student_number = i


print(f'the highest score is student:{first_student_number + 1}  with:  {largest}')
print(f'the  second highest score is student:{second_student_number + 1}  with:  {second_largest}')
