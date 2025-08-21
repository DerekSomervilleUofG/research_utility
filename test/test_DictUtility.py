from unittest import TestCase
from utility.DictUtility import DictUtility

class TestDictUtility(TestCase):

    def test_dict_remove_items(self):
        original = {1:2, 2:3, 3:4, 4:5}
        duplicate = {2:3, 3:5}
        self.assertEqual("dict_keys([1, 4])", str(DictUtility.dict_remove_items(original, duplicate).keys()))