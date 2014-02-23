#!/bin/env python

class Task:
    """
    A class describing a task.
    """

    def __init__(self, name="New task", description="<Not set>", complete=False):
        self._name = name
        self._description = description
        self._complete = complete

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getDescription(self):
        return self._description

    def setDescription(self, description):
        self._description = description

    def getComplete(self):
        return self._complete    

    def setComplete(self, complete):
        self._complete = complete

if __name__ == "__main__":
    print "Test: pyban.py"
    my_task = Task()
    print my_task.getName()
    print my_task.getDescription()
    print my_task.getComplete()
    my_task.setName("Olle")
    my_task.setDescription("Test description")
    my_task.setComplete(True)
    print my_task.getName()
    print my_task.getDescription()
    print my_task.getComplete()
