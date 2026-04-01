def task():
    task=[]#empty list
    print("welcome to the app:")

    total_task=int(input("enter how many task you want to add:"))
    for i in range(1,total_task+1):
        task_name=input(f"enter the task {i} = ")
        task.append(task_name)
    print(f"todays task are \n{task}")

    while True:
        operation=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Stop"))
        if operation==1:
            add=input("Enter the task you want to add=")
            task.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation==2:
            update_val=input("enter the task name you want to update=")
            if update_val in task:
                up=input("enter new task=")