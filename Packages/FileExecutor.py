import os
import pexpect


class FileExecutor:
    @staticmethod
    def get_execution_command(file_path, target_folder):
        _, file_extension = os.path.splitext(file_path)
        if file_extension == ".py":
            return f"python3 {file_path} {target_folder}"
        elif file_extension == ".java":
            return f"java {file_path} {target_folder}"
        elif file_extension == ".c":
            return f"gcc {file_path} -o {os.path.join(target_folder, file_path)}.exe && {os.path.join(target_folder, file_path)}.exe"
        elif file_extension == ".cpp":
            return f"g++ {file_path} -o {os.path.join(target_folder, file_path)}.exe && {os.path.join(target_folder, file_path)}.exe"
        elif file_extension == ".cs":
            return f"dotnet run --project {file_path} {target_folder}"
        else:
            return None

    @staticmethod
    def execute_file(file_path, target_folder):
        execution_command = FileExecutor.get_execution_command(file_path, target_folder)
        if execution_command:
            child = pexpect.spawn(execution_command)
            child.interact()
        else:
            print("Invalid file extension.")



