#!/bin/env python

import unittest
import task

class TaskTestCase(unittest.TestCase):
    def setUp(self):
        self.task1 = task.__init__()
        self.task2 = task.task("test_task", "test_description", True)

    def test_init(self):
        self.assertEquals(self.task1.getName(), "Newtask")
        self.assertEquals(self.task1.getDescription(), "<Not set>")
        self.assertEquals(self.task1.getComplete(), False)
        self.assertEquals(self.task2.getName(), "testtask")
        self.assertEquals(self.task2.getDescription(), "test_description")
        self.assertEquals(self.task2.getComplete(), True)

if __name__ == "__main__":
    unittest.main()
