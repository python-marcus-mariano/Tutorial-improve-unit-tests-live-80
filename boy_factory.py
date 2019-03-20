"""
Factory Boy.
"""

from factory import Factory, Faker

from serial import Task
from fakes import TaskProvider


Faker.add_provider(TaskProvider)


class TaskFactory(Factory):
    """Class Factory tasks."""

    class Meta:
        """Meta Class."""
        model = Task
    
    # Use only Factory boy
    # task_name = 'Dormir'
    # state = 'TODO'

    # Use Factory boy and TaskProvider
    task_name = Faker('task_name')
    state = Faker('state')
