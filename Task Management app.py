def task():
    tasks = []  # empty list
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ").strip()
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        try:
            operation = int(input(
                "Enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit: "
            ))
        except ValueError:
            print("Please enter a number 1–5.")
            continue

        if operation == 1:
            add = input("Enter task you want to add = ").strip()
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ").strip()
            if updated_val in tasks:
                up = input("Enter new task = ").strip()
                tasks[tasks.index(updated_val)] = up
                print(f"Updated task to '{up}'")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Which task you want to delete = ").strip()
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted...")
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice, please select 1–5.")

task()

