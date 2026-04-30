from common.task import Task
from task1.task1 import Task1
from task2.task2 import Task2
from task3.task3 import Task3
from task4.task4 import Task4
from task5.task5 import Task5
from task6.task6a import Task6a
from task6.task6b import Task6b


class LabTask(Task):
    def __init__(self):
        self.labs = [Task1, Task2, Task3, Task4, Task5, Task6a, Task6b]

    def actions(self):
        return [t.as_action() for t in self.labs]
