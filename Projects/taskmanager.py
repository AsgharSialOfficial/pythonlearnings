import os
task_file = 'mytaskmanager.txt'

def load_taks():
    task = []
    if(os.path.exists)(task_file):
        with open(task_file, 'r', encoding='utf-8') as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                task.append({
                    'text':text, "done":status=='done'
                })
    return task
def save_task(task):
    with open('mytaskmanager.txt', 'w', encoding='utf-8') as f:
        for ts in task:
            status = "done" if ts['done'] else "not_done"
            f.write(f'{ts['text']}||{status}\n')


def display_task(task):
    if not task:
        print('No task found')
    else:
        for i,task in enumerate(task, 1):
            checkbox = "✔✔" if task['done'] else " "
            print(f'{i}. [{checkbox}] {task['text']}')


def task_manager():
    task = load_taks()
    while True:
        print('\n --------Task List Manager-------------')
        print('1. Add Task')
        print('2. View Task')
        print('3. Mark as Complete')
        print('4. Delete Task')
        print('5. Exit')

        choice = input('Choose operation from 1-5').strip()
        match choice:
            case "1":
                crtask = input('Enter your task you want to add')
                if crtask:
                    task.append({'text':crtask, 'done':False})
                    save_task(task)
                else:
                    print('your task cannot be empty')
            case "2":
                display_task(task)
            case "3":
                display_task(task)
                try:
                    number = int(input('Enter your task number'))
                    if 1<=number <=len(task):
                        task[number-1]['done']=True
                        save_task(task)
                        print('task marked as done')
                    else:
                        print('Invalid Number')
                except ValueError:
                    print('Enter a Valid Number')


            case "4":
                display_task(task)
                try:
                    number = int(input('Enter your task number to delete'))
                    if 1<=number <=len(task):
                        removed = task.pop(number-1)
                        save_task(task)
                        print('task removed as done')
                    else:
                        print('Invalid Number')
                except ValueError:
                    print('Enter a Valid Number')
            case '5':
                print('Exiting Task Manager')
                break
task_manager()
print('you are outside of task manager')



