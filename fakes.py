"""
Fakes.
"""

from random import choice
from faker import Faker
from faker.providers import BaseProvider
from serial import Task


class TaskProvider(BaseProvider):
    """Class model to provide tasks."""
    
    def task_name(self):
        """Task Names."""
        tasks = ['Acordar', 'Dormir', 'Trabalhar', 'Fazer a live', 'codar']

        return choice(tasks)


    def state(self):
        """State."""        
        state = ['TODO', 'DOING', 'DONE']

        return choice(state)


    def id_(self):
        """Id."""        

        return self.random_int(0, 999)


    def Task(self):
        """Task."""
        return Task(self.task_name(), self.state(), self.id_())        


faker = Faker()
faker.add_provider(TaskProvider)
