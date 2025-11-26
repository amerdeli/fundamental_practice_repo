def to_do_list():
# function handles a to-do list (add/remove task, check list etc.)

    to_do_list = []
    print("================ TO DO LIST ==================") 
    while True:
        print("Select menu:")
        print("1. Add a new task to your list\n"
              "2. Remove a task from your list\n"
              "3. Check open tasks\n"
              "4. Exit")


        while True:
            try:
                selected_option = int(input("Please select one of the above listed options:"))
                if selected_option not in [1, 2, 3, 4]:
                    raise Exception("Request out of range!")
            except ValueError:
                print("Invalid input! Input must be a number!")
            except Exception as e:
                print(e)
            else:
                break
        print("==============================================")        
        if selected_option == 1:
            new_task = input("Enter a new task:")
            to_do_list.append(new_task)
            print("New task has been added!")
            print("==============================================")   
        elif selected_option == 2:
            while True:
                try:
                    task_to_remove = int(input("Enter task index that shall be removed from the list:"))
                    if task_to_remove < 1 or task_to_remove > len(to_do_list):
                        raise Exception("Request out of range!")
                except ValueError:
                    print("Invalid input! Input must be a number!")
                except Exception as e:
                    print(e)
                else:
                    break
            to_do_list.pop(task_to_remove - 1)  
            print("Task has been removed!")
            print("==============================================")          
        elif selected_option == 3:
            if not to_do_list:
                print("No open tasks!")
            else:
                print("Your open tasks:")
                for task_index, task in enumerate(to_do_list, start=1):
                    print(f"{task_index}. {task}")
            print("==============================================")  
        elif selected_option == 4:
            break

to_do_list()
