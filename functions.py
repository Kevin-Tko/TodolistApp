def read_txt(file_name):
    with open(file_name, 'r') as file:
        todos_list = file.readlines()
        return todos_list


def write_txt(file_name, data):
    with open(file_name, 'w') as file:
        file.writelines(data)
