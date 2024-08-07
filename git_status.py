import os
import subprocess
import sys

def get_file_to_commit(dir_name, output):
    operations = ["modified", "added", "deleted"]
    file_suffix = ["py" , "java", "js", "txt", "json", "csv"]
    files = []
    for file in output.split("\n"):
        split_file = file.split(":")
        file_type = ""
        if len(file.strip()) > 0 and file.strip()[0] != "." and "." in file:
            file_type = file.split(".")[1].strip()
            print(dir_name, file_type, file.strip())
        if split_file[0].strip() in operations:
            file_path = split_file[1].strip()          
            if "." != file_path[0]:
                files.append(file_path)
        elif file_type in file_suffix :
            files.append(file.strip())
    return files
    
def check_git_status(base_directory):
    direcotries_to_update = {}
    print("*******************")
    print("****** START ******")
    for dir_name in os.listdir(base_directory):
        dir_path = os.path.join(base_directory, dir_name)
        # Check if the directory contains a .git folder
        if os.path.isdir(os.path.join(dir_path, '.git')):
            print(f"Checking git status in: {dir_path}")
            # Run git status and capture the output
            try:
                result = subprocess.run(['git', '-C', dir_path, 'status'], check=True, capture_output=True, text=True)
                print(result.stdout)
                if "nothing to commit" in result.stdout:
                    direcotries_to_update[dir_name] = "Committed"
                else:
                    direcotries_to_update[dir_name] = get_file_to_commit(dir_name, result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Failed to get git status for {dir_path}: {e}")
                direcotries_to_update.append(dir_name)
    print("Direcotires to commit", direcotries_to_update)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()   
    check_git_status(directory)