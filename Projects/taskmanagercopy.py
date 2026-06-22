import os

def load_task():
    task = []
    with open('mytaskmanagercopy.txt','r', encoding='utf-8') as file:
        for lines in file:
            text, status = lines.strip().rsplit("||", 1)
            task.append({
                'text':text, 'done': status =='done'
            })
    return task

def save_task(task):
    with open('mytaskmanagercopy.txt', 'w', encoding='utf-8') as file:
        for ts in task:
            status = 'done' if ts['done'] else 'not-done'
            file.write(f'{ts['text']}|| {status}\n')
        print('All tasks have been saved!')

def display_task(task):
    if  not task:
        print('your task list is empty')
    else:
        for i, ts in enumerate(task,1):
            checkbox = '✔✔' if ts['done'] else ''
            print(f'{i}.[{checkbox}]: {ts['text']}')
        print('I have listed all the tasks')






def task_managr():
    #task = ['learning python', 'learning DevOps', 'Learning Docker']
    #completed_task = []
    task = load_task()
    print('1. Add Task')
    print('2. View Task')
    print('3. Mark as Completed')
    print('4. Delete Task')
    print('5.Exit')
   

    while True:
        choice = input('Enter your choice number')
        match choice:
            case '1':
                crtask = input('Enter your task')
                task.append({
                    'text':crtask,
                    'done':False
                })
                save_task(task)
            case '2':
                display_task(task)
                print('These are all task')
            case '3':
                number = int(input('Enter task number'))
                if 1<=number <=len(task):
                    task[number-1]['done']=True
                    save_task(task)
                    
                    
            case '4':
                number = int(input('Enter task number'))
                if 1<=number <=len(task):
                    
                   
                    task.pop(number-1)
                    save_task(task)
            case '5':
                print('you are exiting')
                break
print('You have been exited')

task_managr()