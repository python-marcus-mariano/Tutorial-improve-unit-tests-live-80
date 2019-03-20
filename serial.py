"""
Inprove unit tests with Faker

Tutorial-improve-unit-tests-live-80

Homepage and documentation:


License: GNU GENERAL PUBLIC LICENSE Version 3

"""

"""
{id: <int>, task_name: <str>, state: <str>}
"""


class Task():
    """Tipical Class of ORMs."""
    def __init__(self, task_name, state, id_: int = 0):
        """Init."""
        self.id_ = id_
        self.task_name = task_name
        self.state = state

    def __repr__(self):
        """Represetation."""
        return f'Task(task_name="{self.task_name}", state="{self.state}")'


def task_serializer(task: Task) -> dict:
    """Task serializer."""
    return {
        'task_name': task.task_name,
        'state': task.state
    }


def dump_db(db, serializer):
    """Dump DB."""
    return [serializer(obj) for obj in db]
