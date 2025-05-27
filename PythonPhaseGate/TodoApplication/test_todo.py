import todo_function
from unittest.mock import patch
import unittest


class TestTodoApp(unittest.TestCase):
    def test_add_to_my_list(self):
         task = "tega"
         actual=todo_function.add_task(task)
         expected = 'tega'
         self.assertEqual(lens(task), 1)
         #self.assertEqual(,expected)



"
