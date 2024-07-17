from os import getcwd
from utility.ReadWriteFile import ReadWriteFile

class ListReport():

    read_write_file = ReadWriteFile()


    def generate_report_with_name(self, directory, list, file_name):
        if len(list) > 0:
            self.read_write_file.fix_working_directory()
            if directory[-1] != "/":
                directory += "/"
            file = open(directory + file_name, "w",  encoding='utf-8')
            file.write(list[0].get_header() + "\n")
            for item in list:
                file.write(str(item.to_string()) + "\n")
            file.close()

    def generate_report(self, directory, list):
        if len(list) > 0:
            self.generate_report_with_name(directory, list, list[0].get_class_name() + ".csv")
