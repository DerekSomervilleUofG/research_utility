from utility.ReadWriteFile import ReadWriteFile

read_write_file = ReadWriteFile()
FILE_NAME = "log_output.txt"
output_on = True

def log(parameter_one, parameter_two= "", parameter_three=""):
    parameter = f"{parameter_one} {parameter_two} {parameter_three}".strip()
    if output_on:
        print(parameter)
    read_write_file.append_to_file(FILE_NAME, parameter + "\n")

def set_output(on):
    global output_on
    output_on = on