import os

tasks_list = []

def add_new_taks():
    print("======== Task Manager =======")

    while True:
        task = input("Add a new task\n").strip()
     

        if task: # it is checking if task is not empty
               tasks_list.append(task) # adding a new task to task list
               print("Task added successfully!")
               print(f"Your tasks: {tasks_list}")
        else:
             print("Task cannot be empty!")
             continue
        
        while True: # next loop for another task
             next_task = input("\nAdd another task? (y/n) :\n").strip().lower() # another task  - strip() - deleting all white spaces - lower() changing all letters to lowercase

             if next_task in ['y', 'n', 'yes', 'no']: 
                  break
             print("Please enter 'y' or 'n'")
        if next_task in ['n', 'no']:
             print("\n- Final task list", tasks_list)
             save_to_file()
             break

def save_to_file():
    file_path = input("\nEnter file path to save tasks (e. g. teask.txt):").strip()
    if not file_path:
        file_path = "tasks.txt"
    

    try:
        with open(file_path, 'w') as file:
            for i, task in enumerate(tasks_list, 1):
               file.write(f"{i}. {task}\n")
        print(f"Task saved sussessfully to: {os.path.abspath(file_path)}")
    
    except Exception as e:
        print(f"Error saving file: {e}")

add_new_taks()