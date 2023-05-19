import os
import subprocess


class FileExecutor:
    @staticmethod
    def get_execution_command(file_path):
        _, file_extension = os.path.splitext(file_path)
        if file_extension == ".py":
            return f"python {file_path}"
        elif file_extension == ".java":
            return f"java {file_path}"
        elif file_extension == ".c":
            return f"gcc {file_path} -o {file_path}.exe && {file_path}.exe"
        elif file_extension == ".cpp":
            return f"g++ {file_path} -o {file_path}.exe && {file_path}.exe"
        elif file_extension == ".cs":
            return f"dotnet run --project {file_path}"
        else:
            return None