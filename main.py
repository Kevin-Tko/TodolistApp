from functions import read_txt, write_txt
from time_date import time_date

while True:
    print(time_date)
    user_action = input('Type add, show, edit, complete or exit:').lower().strip()

    if user_action.startswith('add'):
        if len(user_action) < 4:
            print('Command is too short. Type add and the too you want to add')
            continue
        else:
            try:
                todos = read_txt('todos.txt')
                ind = len('add')
                todo = user_action[ind:].strip() + '\n'
                todos.append(todo)
                write_txt(file_name='todos.txt', data=todos)
            except ValueError:
                print('Your command is not valid')
                continue


    elif user_action.startswith('show'):
        todos = read_txt('todos.txt')
        todos = [todo.strip('\n') for todo in todos]
        if len(todos) == 0:
            print('No todos')
            continue
        else:
            for index, todo in enumerate(todos):
                print(f'{index + 1}. {todo.capitalize()}')


    elif user_action.startswith('edit'):
        if len(user_action) < 5:
            print('Command too short. Type edit and the todo you want to remove')
            continue
        else:
            try:
                todos = read_txt('todos.txt')
                todos = [todo.strip('\n') for todo in todos]
                ind = len('edit')
                todo = user_action[ind:].strip()
                number = todos.index(todo)
                new_todo = input('Enter a new todo:').lower().strip()
                todos[number] = new_todo
                todos = [todo + '\n' for todo in todos]
                write_txt(file_name='todos.txt', data=todos)
            except ValueError:
                print('Todo not found in the list of todos')
                continue


    elif user_action.startswith('complete'):
        if len(user_action) < 9:
            print('Command too short. Type complete and the todo you want to complete')
            continue
        else:
            try:
                todos = read_txt('todos.txt')
                todos = [todo.strip('\n') for todo in todos]
                ind = len('complete')
                todo = user_action[ind:].strip()
                todo_removed = todos.pop(todos.index(todo))
                print(f'You have completed {todo_removed}')
                todos = [todo + '\n' for todo in todos]
                write_txt(file_name='todos.txt', data=todos)
            except ValueError:
                print('Todo not found in the list of todos')
                continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Invalid action')
