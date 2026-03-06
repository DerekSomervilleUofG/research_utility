from utility.ReadWriteFile import ReadWriteFile

read_write_file = ReadWriteFile()
FILE_NAME = "log_output.txt"

def log(parameter_one, parameter_two= "", parameter_three=""):
    parameters = [str(param) for param in [parameter_one, parameter_two, parameter_three]]
    parameter = " ".join(parameters)
    print(parameter)
    read_write_file.append_to_file(FILE_NAME, parameter + "\n")

