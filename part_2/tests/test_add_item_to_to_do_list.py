import os
from unittest import TestCase
from part_2 import main

class TestAddToToDoList(TestCase):
    def setUp(self):
        f = open('todo.txt', 'w')
        f.write('1\n2\n3')
        f.close()
    def tearDown(self):
        os.remove('todo.txt')

    def test_add_one_item_to_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.add_item_to_do_list('4')
        self.assertEqual(['1', '2', '3', '4'], main.get_to_do_list())
    def test_add_two_item_to_list(self):
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())
        main.add_item_to_do_list('4')
        main.add_item_to_do_list('5')
        self.assertEqual(['1', '2', '3', '4', '5'], main.get_to_do_list())