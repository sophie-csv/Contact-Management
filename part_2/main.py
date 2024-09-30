def get_to_do_list():
    """
    Gets data from todo.txt file an returns it as a list
    :return: list of todo.txt
    """
    f = open('todo.txt', 'r')
    raw_list = f.read()
    f.close()
    return raw_list.split('\n')

def update_to_do_list(to_do_list):
    """
Writes data from todo.txt file based on pram
    :param to_do_list: list to be written to todo.txt file
    :return: updated todo.txt file
    """
    f = open('todo.txt', 'w')
    f.write('\n'.join(to_do_list))
    f.close()

def print_to_do_list():
    """
    prints out the todo.txt file in a readable format
    """
    to_do_list = get_to_do_list()
    for i, item in enumerate(to_do_list):
        print(f'{i + 1}. {item}')

def add_item_to_do_list(item):
    """
    Adds item to todo.txt file
    :param item: item to be added to todo.txt file
    """
    to_do_list = get_to_do_list()
    to_do_list.append(item)
    update_to_do_list(to_do_list)

def remove_item_from_todo_list(item):
    """
    Removes item from todo.txt file
    :param item: Item to be removed from todo.txt file
    """
    to_do_list = get_to_do_list()
    if item not in to_do_list:
        print(f'{item} not in todo list.')
        return
    to_do_list.remove(item)
    update_to_do_list(to_do_list)

# while True:
#     print_to_do_list()
#     choice = input('Enter 1 to add an item or enter 2 to remove an item from the todo list: ')
#     print()
#     if choice == '1':
#         new_item = input('Add Item to todo list: ')
#         add_item_to_do_list(new_item)
#     elif choice == '2':
#         remove_item = input('Remove Item from todo list: ')
#         remove_item_from_todo_list(remove_item)
#     print()

