import os
from unittest import TestCase
from part_2 import main

class TestUpdateToDoList(TestCase):
    def setUp(self):
        f = open('todo.txt', 'w')
        f.close()
    def tearDown(self):
        os.remove('todo.txt')

    def test_update_to_do_list_one_item_in_list(self):
        self.assertEqual([''], main.get_to_do_list())
        main.update_to_do_list(['1'])
        self.assertEqual(['1'], main.get_to_do_list())

    def test_update_to_do_list_two_item_in_list(self):
        self.assertEqual([''], main.get_to_do_list())
        main.update_to_do_list(['1', '2'])
        self.assertEqual(['1', '2'], main.get_to_do_list())

    def test_update_to_do_list_three_item_in_list(self):
        self.assertEqual([''], main.get_to_do_list())
        main.update_to_do_list(['1', '2', '3'])
        self.assertEqual(['1', '2', '3'], main.get_to_do_list())

    def test_update_to_do_list_no_item_in_list(self):
        self.assertEqual([''], main.get_to_do_list())
        main.update_to_do_list([])
        self.assertEqual([''], main.get_to_do_list())

