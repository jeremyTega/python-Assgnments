def call_names(number = 10):
   return  f"the square of {number} is {number ** 2}"


userNumer = int(input("enter your number: "))
print(call_names(userNumer))
def print_args(*args, **kwargs):
*args: Allows a function to accept any number of positional arguments.
**kwargs: Allows a function to accept any number of keyword arguments.
