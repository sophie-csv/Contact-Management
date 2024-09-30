import os
from unittest import TestCase
from part_2 import main

class TestGetToDoList(TestCase):
    def setUp(self):
        f = open('todo.txt', 'w')
        f.write('1\n2\n3')
        f.close()

    def tearDown(self):
        os.remove('todo.txt')
    def test_get_to_do_list(self):
        self.assertEqual(main.get_to_do_list(), ['1', '2', '3'])