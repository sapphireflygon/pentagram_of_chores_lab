import unittest
from classes.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.wash_dishes = Task("Wash the dishes", 15)
        self.cook_dinner = Task("Cook dinner", 45)
        self.clean_windows = Task("Clean windows", 30)

    # @unittest.skip("Delete this line to run the test")
    def test_description(self):
        self.assertEqual("Cook dinner", self.cook_dinner.description)

    # @unittest.skip("Delete this line to run the test")
    def test_duration(self):
        self.assertEqual(15, self.wash_dishes.duration)