import streamlit as st
from functions import read_txt, write_txt

todos = read_txt('todos.txt')

background_color = """
    <style>
        [data-teststate="notRunning"] {
        background-color:#15202b;
        }
        [data-testid="StyledLinkIconContainer"] {
        color:#e6ffcc;
        font-family:Garamond;
        font-size:8;
        }
        [data-testid="stMarkdownContainer"] {
        color:white;
        font-family:Garamond;
        }
        [data-testid="stHeader"] {
        background-color:#f5e6ff;
        font-family:Garamond;
        }
    </style>
"""
st.markdown(background_color, unsafe_allow_html=True)


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    write_txt(file_name='todos.txt', data=todos)
    st.session_state['new_todo'] = ''


st.title('Todo App - Organize Your Day 📝')
st.subheader('Enter your todos through the text box & complete by ticking the checkbox')
st.write('This App will improve your productivity & help you keep track of your daily activities')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_txt(file_name='todos.txt', data=todos)
        del st.session_state[todo]
        st.experimental_rerun()  # Reruns the app

st.text_input('Enter A Todo', placeholder='enter a todo', max_chars=35, on_change=add_todo, key='new_todo')
