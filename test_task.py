#!/bin/env python3

from pyban import Task
import unittest

class TestPyBanTask(unittest.TestCase):
    """
    This test case tests the Task class of pyban.
    """

    def test_new_task(self):
        test_task = Task()
        self.assertEqual(test_task.get_name(), "New Task")

    def test_new_named_task(self):
        test_task = Task("Test Task")
        self.assertEqual(test_task.get_name(), "Test Task")

    def test_task_set_name(self):
        test_task = Task()
        test_task.set_name("Name set")
        self.assertEqual(test_task.get_name(), "Name set")

    def test_task_set_description(self):
        test_task = Task()
        test_task.set_description("Desc set")
        self.assertEqual(test_task.get_description(), "Desc set")

if __name__ == "__main__":
    unittest.main()
