from utility.UtilityText import UtilityText

from unittest import TestCase


class TestUtilityText(TestCase):

    utility_text = UtilityText()

    def test_get_non_blank_lines(self):
        content = "Derek\n\nSomerville\n\n\n"
        self.assertEqual(2, len(self.utility_text.get_non_blank_lines(content)))

    def test_case_to_word_snake(self):
        self.assertEqual(["snake", "case"], self.utility_text.case_to_word("snake_case"))

    def test_case_to_word_camel(self):
        self.assertEqual(["camel", "case"], self.utility_text.case_to_word("camelCase"))


    def test_break_snake_case(self):
        self.assertEqual(["snake", "case"], self.utility_text.break_snake_case("snake_case"))

    def test_break_camel_case(self):
        self.assertEqual(["camel", "case"], self.utility_text.break_camel_case("camelCase"))
