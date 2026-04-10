def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        pass  # If file doesn’t exist, start empty
    return tasks


def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def display_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!\n")
    else:
        print("\nYour to-do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()


def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")


def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)

        elif choice == '2':
            add_task(tasks)
            save_tasks(filename, tasks)

        elif choice == '3':
            remove_task(tasks)
            save_tasks(filename, tasks)

        elif choice == '4':
            save_tasks(filename, tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()