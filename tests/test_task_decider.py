import unittest
from classes.task import Task
from classes.task_decider import *

class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.wash_dishes = Task("Wash the dishes", 15)
        self.cook_dinner = Task("Cook dinner", 45)
        self.clean_windows = Task("Clean windows", 30)
        self.wash_clothes = Task("Wash clothes", 60)
        self.do_ironing = Task("Do ironing", 20)

    # @unittest.skip("Delete this line to run the test")
    def test_prefer_wash_dishes_over_cook_dinner__true(self):
        preferred_task = get_preferred_option(self.wash_dishes.description, self.cook_dinner.description)
        self.assertEqual("Wash the dishes", preferred_task)

    # @unittest.skip("Delete this line to run the test")
    def test_prefer_cook_dinner_over_clean_windows__true(self):
        preferred_task = get_preferred_option(self.clean_windows.description, self.cook_dinner.description)
        self.assertEqual("Cook dinner", preferred_task)

    # @unittest.skip("Delete this line to run the test")
    def test_prefer_clean_windows_over_wash_dishes__true(self):
        preferred_task = get_preferred_option(self.wash_dishes.description, self.clean_windows.description)
        self.assertEqual("Clean windows", preferred_task)

    # @unittest.skip("Delete this line to run the test")
    def test_prefer_wash_clothes_over_cook_dinner(self):
        preferred_task = get_preferred_option(self.wash_clothes.description, self.cook_dinner.description)
        self.assertEqual("Wash clothes", preferred_task)

    # @unittest.skip("Delete this line to run the test")
    def test_prefer_wash_clothes_over_clean_windows(self):
        preferred_task = get_preferred_option(self.clean_windows.description, self.wash_clothes.description)
        self.assertEqual("Wash clothes", preferred_task)

    # @unittest.skip("Delete this line to run the test")
    def test_prefer_do_ironing_over_wash_clothes(self):
        preferred_task = get_preferred_option(self.wash_clothes.description, self.do_ironing.description)
        self.assertEqual("Do ironing", preferred_task)

    # @unittest.skip("Delete this line to run the test")
    def test_prefer_do_ironing_over_wash_dishes(self):
        preferred_task = get_preferred_option(self.do_ironing.description, self.wash_dishes.description)
        self.assertEqual("Do ironing", preferred_task)