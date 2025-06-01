import os

todo_list = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ui():
    clear_screen()
    print("📋 To-Do List (Console Version)\n")
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    print("\nOptions:")
    print("1 - Add Task")
    print("2 - Remove Task")
    print("3 - Exit")

def add_task():
    task = input("Enter a new task: ")
    if task:
        todo_list.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")
    input("Press Enter to continue...")

def remove_task():
    if not todo_list:
        print("No tasks to remove.")
        input("Press Enter to continue...")
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")
    input("Press Enter to continue...")

# Main loop
while True:
    print_ui()
    choice = input("\nSelect an option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        clear_screen()
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
        input("Press Enter to continue...")
