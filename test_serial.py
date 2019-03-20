"""
Test Serial.
"""

from unittest import TestCase, main
from serial import Task, task_serializer, dump_db
from fakes import faker
from boy_factory import TaskFactory


class TestModelTask(TestCase):
    """Class Test Model Task."""
    
    def test_check_model_representation(self):
        """Test Representation model."""
        esperado = 'Task(task_name="Acordar", state="TODO")'
        chamada = Task('Acordar', 'TODO')

        self.assertEqual(esperado, str(chamada))

    def test_check_model_has_id_and_his_id_is_int(self):
        """Test Id."""
        chamada = Task('', '')

        self.assertIsInstance(chamada.id_, int)


class TestTaskSerializer(TestCase):
    """Class Test Serializer Task."""
    
    def test_task_serializer_must_be_a_dict(self):
        """Test seiralizer is dict."""
        task_name = 'Ligar para o Will'
        state = 'TODO'

        task = Task(task_name, state)

        self.assertIsInstance(task_serializer(task), dict)

    
    def test_task_serializer_do_not_serialize_a_none_task_type(self):
        """Test seiralizer is not serialize a none type task."""
        task_name = 'Ligar para o Will'
        
        with self.assertRaises(AttributeError):
            task_serializer(task_name)


class TestDumpDB(TestCase):
    """Class Test Dump DB."""
    
    def test_serializer_must_be_transform_all_data_in_dict(self):
        """Test seiralizer transform data in dict."""
        
        # Use only fakes
        # fake_tasks = [faker.Task() for i in range(10)]
        # import ipdb; ipdb.set_trace()
        
        # User Fakes and Factory Boy
        fake_tasks = TaskFactory.create_batch(10)
       
        results = dump_db(fake_tasks, task_serializer)

        for r in results:
            with self.subTest(r=r):
                self.assertIsInstance(r, dict)


if __name__ == "__main__":
    main()
