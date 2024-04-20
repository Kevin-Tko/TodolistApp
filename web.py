import streamlit as st
from functions import read_txt, write_txt

todos = read_txt('todos.txt')

background_color = """
    <style>
        [data-teststate="notRunning"] {
        background-color:#15202b;
        color:white;
        }
        [data-testid="StyledLinkIconContainer"] {
        color:white;
        }
        [data-testid="stMarkdownContainer"] {
        color:white;
        }
        [data-testid="stHeader"] {
        background-color:#f5e6ff;
        }
    </style>
"""
st.markdown(background_color, unsafe_allow_html=True)


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    write_txt(file_name='todos.txt', data=todos)
    st.session_state['new_todo'] = ''


st.title('Elephant Man Todo App')
st.subheader('This is a Todo App')
st.write('This App will improve your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_txt(file_name='todos.txt', data=todos)
        del st.session_state[todo]
        st.experimental_rerun()  # Reruns the app

st.text_input('Enter A Todo', placeholder='enter a todo', max_chars=35, on_change=add_todo, key='new_todo')
