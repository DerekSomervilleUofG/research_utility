from unittest import TestCase
from utility.ReadWriteFile import ReadWriteFile
import os

#TODO: Lots of hardcoded results that could change place
class TestReadWriteFile(TestCase):

    read_write_file = ReadWriteFile()
    read_write_file.fix_working_directory()
    
    def test_fix_site_packages_directory(self):
        self.assertEqual("C:/Users/Derek Somerville/Documents/Lecturer/marking", self.read_write_file.fix_site_packages_directory(r"C:\Users\Derek Somerville\Documents\Lecturer\marking\venv\Lib\site-packages"))
    
    def test_top_directory(self):
        self.assertEqual("utility", self.read_write_file.get_top_level_dir().replace("\\","/").split("/")[-2])
    
    def test_fix_working_directory(self):
        self.read_write_file.fix_working_directory()
        self.assertEqual("utility", os.getcwd().replace("\\","/").split("/")[-1])

    def test_open_file(self):
        self.read_write_file.fix_working_directory()
        file_name = "README.md"
        file = self.read_write_file.open_file("", file_name)
        self.assertEqual(file_name, file.name)
        file.close()

    def test_read_csv(self):
        self.read_write_file.fix_working_directory()
        file = self.read_write_file.open_file("resource/test/mocklab", "test_mocklab.csv")
        file_data = self.read_write_file.read_csv(file)
        self.assertEqual(2, len(file_data))

    def test_get_file_as_csv(self):
        self.read_write_file.fix_working_directory()
        file_data = self.read_write_file.get_file_as_csv("test_mocklab.csv", "resource/test/mocklab")
        self.assertEqual(2, len(file_data))

    def test_get_file_as_csv_no_directory(self):
        file_data = self.read_write_file.get_file_as_csv("test/mocklab/test_mocklab.csv")
        self.assertEqual(2, len(file_data))

    def test_get_file_as_string(self):
        self.read_write_file.fix_working_directory()
        file_data = self.read_write_file.get_file_as_string("test_mocklab.csv", "resource/test/mocklab")
        self.assertEqual(str, type(file_data))
        
    def test_get_file_as_string_text(self):
        self.read_write_file.fix_working_directory()
        file_data = self.read_write_file.get_file_as_string("test_mocklab.csv", "resource/test/mocklab")
        self.assertEqual('"TDD Card Game"', file_data.split("\n")[1].split(",")[1])

    def test_write_file(self):
        file_name = "test.txt"
        content = "hello"
        self.read_write_file.write_file(file_name, content)
        self.assertEqual(content, self.read_write_file.get_file_as_string(file_name))
        self.read_write_file.remove_files(file_name, "resource")

    def test_write_csv(self):
        file_name = "test.txt"
        content = [["hello,world"]]
        self.read_write_file.write_csv(file_name, content)
        self.assertEqual(1, len(self.read_write_file.get_file_as_csv(file_name)))


    def test_get_list_of_directories_with_search(self):
        self.read_write_file.fix_working_directory()
        directories = self.read_write_file.get_list_of_directories_with_search("resource","test")
        self.assertIn("test", directories)

    def test_get_list_of_directories(self):
        self.read_write_file.fix_working_directory()
        directories = self.read_write_file.get_list_of_directories("resource")
        self.assertIn("test", directories)

    def test_get_list_from_directory(self):
        self.read_write_file.fix_working_directory()
        directories = self.read_write_file.get_list_from_directory("resource/")
        self.assertIn("test.txt", directories)

    def test_get_list_of_file(self):
        self.read_write_file.fix_working_directory()
        files = self.read_write_file.get_list_of_file("resource/test/mocklab/", "csv")
        self.assertIn("resource/test/mocklab/test_mocklab.csv", files)

    def test_get_list_of_file_from_sub_directory(self):
        self.read_write_file.fix_working_directory()
        files = self.read_write_file.get_list_of_file_from_sub_directory("resource/")
        self.assertIn("test_mocklab.csv", files)

    def test_get_list_of_file_from_sub_directory_with_path(self):
        self.read_write_file.fix_working_directory()
        files = self.read_write_file.get_list_of_file_from_sub_directory_with_path("resource/", "csv")
        self.assertIn("test/mocklab/test_mocklab.csv", files)

    def test_remove_files(self):
        pass

    def test_file_exists(self):
        self.assertTrue(self.read_write_file.file_exists("test_mocklab.csv", "resource/test/mocklab/"))

    def test_dir_exists(self):
        self.assertTrue(self.read_write_file.dir_exists( "resource/test/mocklab/"))

    def test_get_directory_with_directories(self):
        directories = ["test", "mocklab"]
        self.assertEqual("resource/test/mocklab/", self.read_write_file.get_directory_with_directories("resource/", directories))