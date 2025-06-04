import todo_function


def mainFunction():
       while True:
        todo_function.display_menu()

        choice = int(input("Enter your choice: "))
        if choice == 1:
            task = input("Enter the task: ")
            todo_function.add_task(task)
        elif choice == 2:
                todo_function.view_tasks()
        elif choice == 3:
                mark_task_complete()
        elif choice == 4:
                task_number = int(input("\nEnter the task number to delete: "))
                todo_function.delete_task(task_number)
        elif choice == 5:
            print("Good Bye.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

print(mainFunction())


class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance <= 100:
            raise ValueError("Balance must be greater than N100.")
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount % 500 != 0 and amount % 1000 != 0:
            print("Please enter an amount that is a multiple of 500 or 1000.")
            return False

        if amount > self.balance:
            print("Insufficient funds.")
            return False

        if amount > 20000:
            print("The maximum amount you can withdraw at once is N20,000.")
            return False

        fee = 100
        total_deduction = amount + fee
        if total_deduction > self.balance:
            print("Insufficient funds to cover withdrawal and fee.")
            return False

        self.balance -= total_deduction
        print(f"Transaction successful. You withdrew N{amount}.")
        print(f"Withdrawal fee is: N{fee}")
        print(f"Your new balance is N{self.balance}.")
        return True

    def get_balance(self):
        return self.balance
