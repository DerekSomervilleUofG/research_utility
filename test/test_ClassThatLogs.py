from unittest import TestCase
from utility.ClassThatLogs import ClassThatLogs


class TestClassThatLogs(TestCase):

    def test_to_string(self):
        class_that_logs = ClassThatLogs()
        self.assertEqual("ClassThatLogs", class_that_logs.get_class_name())
