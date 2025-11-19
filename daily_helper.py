
tasks = []

def display_menu():
    print("\n--- Daily Helper To-Do List Menu ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as Done (Delete)")
    print("4. Exit Application")
    print("------------------------------------")

def add_task():
    task_description = input("Enter the new task: ")
    if task_description.strip():
        tasks.append(task_description.strip())
        print(f"✅ Task '{task_description}' added successfully.")
    else:
        print("❌ Task cannot be empty. Please try again.")

def view_tasks():
    if not tasks:
        print("🎉 Your list is empty! Enjoy your free time.")
        return
    
    print("\n--- Current To-Do List ---")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    print("--------------------------")

def delete_task():
    view_tasks()
    
    if not tasks:
        return
        
    try:
        task_num_input = input("Enter the number of the task you finished/want to delete: ")
        
        task_index = int(task_num_input) - 1
        
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"🗑️ Task '{deleted_task}' marked as done and removed.")
        else:
            print(f"⚠️ Invalid number: '{task_num_input}'. Please enter a number from 1 to {len(tasks)}.")

    except ValueError:
        print("❌ Invalid input. Please enter a numerical task number.")

def run_daily_helper():
    choice = 0
    while choice != 4:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("👋 Thank you for using Daily Helper. Exiting the application.")
        else:
            print("🤔 That choice doesn't exist. Please try a number between 1 and 4.")

if __name__ == "__main__":
    run_daily_helper()