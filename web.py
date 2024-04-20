import streamlit as st
from functions import read_txt, write_txt

todos = read_txt('todos.txt')


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    write_txt(file_name='todos.txt', data=todos)

st.title('Elephant Man Todo App')
st.subheader('This is Todo App')
st.write('This App will improve your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_txt(file_name='todos.txt', data=todos)
        del st.session_state[todo]
        st.experimental_rerun() # Reruns the app

st.text_input('Enter A Todo', placeholder='enter a todo', max_chars=35, on_change=add_todo,key='new_todo')
