print("|-------------------------------|") #30
print("|           TO DO APP           |")
print("|-------------------------------|")
print("""|    1. Add a Task              |
|    2. Remove a Task           |
|    3. List all Tasks          |
|    4. Remove all Tasks        |
|    0. Exit                    |
|_______________________________|    """)


tasks_list = []
next_idx = 0
curr_idx = 0

def add_task(new_task) :
    task_list[next_idx] = new_task
    curr_idx = next_idx
    next_idx += 1
    print(f"New task added: {curr_idx} - {new_task}")

def remove_task(del_task_idx) :
    if del_task_idx < len(tasks_list):



        
        # Left here



        
    elif len(tasks_list < 1):
        print("The List is empty!")
    else :
        print("Invalid Index!")

while True: 
    option = int(input("\nWhat do you want to do? : "))

    match option:
        case 1:
            new_task = input("New Task: ")
            add_task(new_task)
        case 2:
            del_task_idx = int(input("Enter Task Index to Remove: "))
            remove_task(del_task_idx)
        case 3:
            list_all_tasks()
        case 4:
            remove_all_tasks()
        case 0:
            print("\nExiting the App...")
            break
        case _:
            print("Invalid Option!")
