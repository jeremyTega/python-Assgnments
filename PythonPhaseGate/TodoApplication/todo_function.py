# tasks.append({"task": task, "completed": False})
todo_task = []

def display_menu():
    print("""

                       MAIN MENU

                  1  -> Add Task
                  2  -> view all task
                  3  -> mark a task
                  4  -> Delete a task
                  0  -> Exit
            ======================================
                Kindly enter your choice below:
            ======================================
        """)

def view_tasks():
    print(todo_task)


def add_task(task):
    # task = input("Enter the task: ")
    if task:
        todo_task.append(task)
        view_tasks
        print("Task  successfully added.")
    else:
        print("Task cannot be empty.")





def delete_task(tasks):
    view_tasks()
    if tasks:
        if 1 <= tasks <= len(tasks):
                deleted_task = todo_task.pop(task_number - 1)
                print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
                print("Invalid task number!")


def mark_task_complete(tasks):
    view_tasks(tasks)
    if tasks:
















