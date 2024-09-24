from unittest import TestCase
from utility.ListUtility import ListUtility

class TestListUtility(TestCase):
    
    def test_merge_list(self):
        start_list = [1, 2, 3]
        append_list = [3, 4, 5]
        self.assertEqual([1, 2, 3, 4, 5], ListUtility.merge_list(start_list, append_list))
    
    
    def test_merge_list_same(self):
        start_list = [1, 2, 3]
        append_list = [1, 2, 3]
        self.assertEqual([1, 2, 3], ListUtility.merge_list(start_list, append_list))