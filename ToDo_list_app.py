# To do list

import json

file_name="todo_list.json"


def load_tasks():
    try:
        with open(file_name,'r') as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name,'w') as file:
            return json.dump(tasks,file)
        
    except:
        print("failed to save")


def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")


def create_tasks(tasks):
    description=input("enter an task description: ").strip()
    if description:
        tasks["tasks"].append({"description":description, "complete": False})
        save_tasks(tasks)

    else:
        print("Description cannot be empty")


def mark_as_complete(tasks):
    view_tasks(tasks)
    print()
    try:
        task_num=int(input("enter the task number: ").strip())
        if 1<=task_num<=len(tasks["tasks"]):
            tasks["tasks"][task_num-1]["complete"]=True
            save_tasks(tasks)
            print("Marked as completed")
        else:
            print("invalid task number")

    except:
        print("invalid input")



def main():
    
    tasks=load_tasks()
    
    

    while True:
        print("\nTo-do List Manager")
        print("1.View tasks")
        print("2.Add tasks")
        print("3.Complete task")
        print("4.Exit")


        choice=input("Enter your option:  ").strip()

        if choice=="1":
            view_tasks(tasks)

        elif choice=="2":
            create_tasks(tasks)

        elif choice=="3":
            mark_as_complete(tasks)

        elif choice=="4":
            print("goodbye")
            break
        else:
            print("not a valid input")

main()



## HW
# ADD functions to delete & mark as pending