def categorize_numbers(*args, divisible_by=2):
    for num in args:
        if num % divisible_by==0:
            print(num)
        else:
            print("no divisible numbers found")

categorize_numbers(10,15,21,30, divisible_by=5)
