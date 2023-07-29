# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

def add(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to your To-Do list.")

def view():
    if not tasks:
        print("\nThe To-Do list is empty.")
    else:
        print("\nTo-Do List:")
        for num, task in enumerate(tasks, 1):
            print(f"{num}. {task}")

def remove(task_index):
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
            task = input("Enter the task you want to add: ")
            add(task)
        elif choice == "2":
            view()
        elif choice == "3":
            view()
            task_index = int(input("Enter the numered task you want to remove: "))
            remove(task_index)
        elif choice == "4":
            print("Exiting the To-Do list application.")
            break
        else:
            print("Invalid choice. Please enter a valid value.")

if __name__ == "__main__":
    main()
