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
