import csv
import os
import subprocess
import stat
import pathlib
import glob
from utility.ClassThatLogs import ClassThatLogs
import shutil


def handleGitPermissionError(func, path, exception):
    if exception[0] == PermissionError and ".git" in path:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    else:
        raise


class ReadWriteFile(ClassThatLogs):

    file_path_prefix = "resource/"
    top_level_dir = None
    
    def fix_site_packages_directory(self, directory):
        parts = directory.replace("\\","/").split("/")
        if parts[-1] == "site-packages":
            directory = "/".join(parts[:-3])
        return directory
    
    def get_top_level_dir(self):
        if self.top_level_dir is None:
            self.top_level_dir = self.fix_site_packages_directory(str(pathlib.Path(__file__).parent.parent.resolve())) + "/"
        return self.top_level_dir

    def fix_working_directory(self):
        os.chdir(self.get_top_level_dir())

    def get_directory_with_directories(self, base_directory, directories ):
        return base_directory + ''.join(map(lambda dir: dir + "/", directories))
    
    def create_path_and_open_file(self,directory, file_name, operation):
        if "/" in file_name:
            folders = file_name.split("/")
        else:
            folders = file_name.split("\\")
        working_directory = os.getcwd()
        os.chdir(directory)
        self.make_folders(folders[0:-1])
        open_file = open(directory + file_name, operation, encoding = 'utf-8')
        os.chdir(working_directory)
        return open_file

    def open_file(self, directory, file_name, operation="rt"):
        open_file = None
        if directory is None or directory == "":
            directory = ""
        elif (directory[-1] != "/" and directory[-1] != "\\"):
            directory += "/"
        try:
            if operation == "w":
                open_file = open(directory + file_name, operation, encoding='utf-8', errors='ignore', newline='\n')
            else:
                open_file = open(directory + file_name, operation, encoding='utf-8', errors='ignore')
        except:
            print("ReadWriteFile.open_file", directory, file_name)
            open_file = self.create_path_and_open_file(directory, file_name, operation)

        return open_file

    def read_csv(self, open_file):
        file_data = []
        file_reader = csv.reader(open_file)
        for row in file_reader:
            file_data.append(row)
        open_file.close()
        return file_data

    def get_file_as_csv(self, file_name, directory=None):
        if directory is None:
            directory = self.file_path_prefix
            self.fix_working_directory()
        data_file = self.open_file(directory, file_name)
        return self.read_csv(data_file)

    def get_file_as_csv_with_directories(self, file_name, base_directory, directories):
        return self.get_file_as_csv(file_name, self.get_directory_with_directories(base_directory, directories))
    
    def get_file_as_string(self, file_name, directory=None):
        if directory is None:
            directory = self.file_path_prefix
            self.fix_working_directory()
        data_file = self.open_file(directory, file_name)
        content = data_file.read()
        data_file.close()
        return content

    def get_file_as_string_with_directories(self, file_name, base_directory, directories):
        return self.get_file_as_string(file_name, self.get_directory_with_directories(base_directory, directories))
   

    def get_file_as_lines(self, file_name, directory=None):
        try:
            data_file = self.open_file(directory, file_name)
            lines = data_file.readlines()
            data_file.close()
        except UnicodeDecodeError:
            print("ReadWriteFile.open_file", file_name)
            raise
        return lines

    def get_file_as_lines_with_directories(self, file_name, base_directory, directories):
        return self.get_file_as_lines(file_name, self.get_directory_with_directories(base_directory, directories))
   
    def write_csv(self, file_name, csv_rows, directory=None):
        content = ""
        for row in csv_rows:
            content += ",".join(row) + "\n"
        self.write_file(file_name, content, directory)

    def write_file(self, file_name, content, directory=None):
        if directory is None:
            directory = self.file_path_prefix
            self.fix_working_directory()
        write_file = self.open_file(directory, file_name, "w")
        write_file.write(content)
        write_file.close()

    def append_to_file(self, file_name, content, directory=None):
        if directory is None:
            directory = self.file_path_prefix
            self.fix_working_directory()
        write_file = self.open_file(directory, file_name, "a")
        write_file.write(content)
        write_file.close()

    def make_folders(self, folders):
        path = os.getcwd()
        for folder in folders:
            path += "/" + folder
            if not self.dir_exists(path):
                os.mkdir(path)
        return path

    def write_csv(self, file_name, content, directory=None):
        csv_format = ""
        for row in content:
            line = ""
            for column in row:
                line += str(column) + ","
            csv_format += line + "\n"
        self.write_file(file_name, csv_format, directory)

    def get_list_of_directories_with_search(self, path, search_term):
        return [directory for directory in os.listdir(path) if search_term in directory]

    def get_list_of_directories(self, path):
        return [directory for directory in next(os.walk(path))[1]]

    def get_list_from_directory(self, path):
        return [directory for directory in os.listdir(path)]

    def get_list_of_file(self, path, file_type):
        files = [i.replace("\\", "/") for i in glob.glob(path + "*." + file_type)]
        return files

    def get_list_of_file_from_sub_directory(self, path):
        all_files = []
        for root, directory, files in os.walk(path):
            all_files += files
        return all_files

    def get_list_of_file_from_sub_directory_with_path(self, path, file_type):
        all_files = []
        for root, directory, files in os.walk(path):
            for file_name in files:
                if file_type in file_name:
                    file_path = root.replace(path, "") + "/" + file_name
                    all_files.append(file_path.replace("\\", "/").replace("//", "/"))
        return all_files

    def remove_files(self, file_search, directory=""):
        for file in glob.glob(directory + file_search):
            os.remove(file)

    def file_exists(self, file_name, directory=""):
        if len(directory) > 1 and ("/" != directory[-1] or "\\" != directory[-1]):
            directory += "/"
        return os.path.isfile( directory + file_name)

    def dir_exists(self, directory):
        return os.path.isdir(directory)

    def create_directory(self, directory):
        os.makedirs(directory, exist_ok=True)

    def delete_directory(self, directory):
        if self.dir_exists(directory):
            shutil.rmtree(directory, ignore_errors=False, onerror=handleGitPermissionError)

    def delete_directory_all(self, directory):
        try:
            os.chmod(directory, 0o777)
            for path in glob.glob(directory):
                shutil.rmtree(path, ignore_errors=False, onerror=handleGitPermissionError)
        except OSError as exp:
            print(f'Error: {exp.strerror}')
            if os.name == 'nt':
                subprocess.Popen("rd /s /q " + directory, shell=True, stdout=subprocess.PIPE)
            else:
                subprocess.Popen("rm -rf " + directory, shell=True, stdout=subprocess.PIPE)

    def delete_file(self, file_name, directory = ""):
        if directory != "":
            file_path = directory + "/" + file_name
        else:
            file_path = file_name
        if os.path.isfile(file_path):
            os.remove(file_path)

    def delete_file_type(self, directory, file_type):
        files = self.get_list_of_file(directory, file_type)
        for file in files:
            self.delete_file(file, "")

    def make_path_absolute(self, path):
        if type(path) == str:
            path = pathlib.Path(path).resolve()
        path = str(path.absolute()).replace("\\", "/").replace("//", "/")
        if not path.endswith("/"):
            path += "/"
        return path
