# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the To-Do list.")

def view_tasks():
    if not tasks:
        print("The To-Do list is empty.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' has been removed from the To-Do list.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_index = int(input("Enter the task number to remove: "))
            remove_task(task_index)
        elif choice == "4":
            print("Exiting the To-Do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
