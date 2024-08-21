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

    def test_get_default_repo(self):
        url = "https://git.dcs.gla.ac.uk/DerekSomerville/utility"
        self.assertEqual(url, self.utility_text.get_default_repo(url))
        
    def test_get_default_repo_user_name(self):
        url = "https://git.dcs.gla.ac.uk/DerekSomerville/utility"
        self.assertEqual(url.replace("//", "//DerekSomerville@"), self.utility_text.get_default_repo(url, "DerekSomerville"))
        
    def test_get_default_repo_access_token(self):
        url = "https://git.dcs.gla.ac.uk/DerekSomerville/utility"
        self.assertEqual(url.replace("//", "//DerekSomerville:1234@"), self.utility_text.get_default_repo(url, "DerekSomerville", "1234"))
        
    def test_formate_text(self):
        self.assertEqual("Derek", UtilityText.formate_text("Derek"))
        
    def test_formate_text_single(self):
        self.assertEqual("Derek", UtilityText.formate_text('Derek'))