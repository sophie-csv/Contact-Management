def get_to_do_list():
    f = open('todo.txt', 'r')
    raw_list = f.read()
    f.close()
    return raw_list.split('\n')

def print_to_do_list():
    to_do_list = get_to_do_list()
    for i, item in enumerate(to_do_list):
        print(f'{i + 1}. {item}')

def add_item_to_do_list(item):
    to_do_list = get_to_do_list()
    to_do_list.append(item)
    f = open('todo.txt', 'w')
    f.write('\n'.join(to_do_list))
    f.close()

def remove_item_from_todo_list(item):
    to_do_list = get_to_do_list()
    if item in to_do_list:
        print({item} 'not in todo list.')
        return
    to_do_list.remove(item)
    f =

while True:
    print_to_do_list()
    new_item = input('Add Item to todo list: ')
    add_item_to_do_list(new_item)


