import os
from unittest import TestCase
from part_2 import main

class TestRemoveFromToDoList(TestCase):
    def setUp(self):
        f = open('todo.txt', 'w')
        f.write('1\n2\n3')
        f.close()
    def tearDown(self):
        os.remove('todo.txt')

    def test_remove_front_item_from_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.remove_item_from_todo_list('1')
        self.assertEqual(['2', '3'], main.get_to_do_list())

    def test_remove_back_item_from_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.remove_item_from_todo_list('3')
        self.assertEqual(['1', '2'], main.get_to_do_list())

    def test_remove_middle_item_from_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.remove_item_from_todo_list('2')
        self.assertEqual(['1', '3'], main.get_to_do_list())

    def test_remove_two_items_in_succession_from_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.remove_item_from_todo_list('1')
        main.remove_item_from_todo_list('2')
        self.assertEqual(['3'], main.get_to_do_list())

    def test_remove_all_item_from_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.remove_item_from_todo_list('1')
        main.remove_item_from_todo_list('2')
        main.remove_item_from_todo_list('3')
        self.assertEqual([''], main.get_to_do_list())

    def test_remove_item_from_list_after_added_item(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.add_item_to_do_list('4')
        main.remove_item_from_todo_list('2')
        self.assertEqual(['1', '3', '4'], main.get_to_do_list())

    def test_remove_item_not_in_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.remove_item_from_todo_list('4')
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())

    def test_remove_many_items_not_in_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.remove_item_from_todo_list('4')
        main.remove_item_from_todo_list('5')
        main.remove_item_from_todo_list('6')
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())

