import os
import json
import time
from ui.menu import Menu
from blessed import Terminal
import pexpect
from .FileExecutor import FileExecutor
import colorama
class Packager:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.menu = None
        self.terminal = Terminal()
        self.FileExecutor = FileExecutor()
        self.run()

    def get_packages_path(self):
        current_path = os.getcwd()
        packages_path = os.path.join(current_path, "Packages")
        return packages_path

    def get_folders(self):
        packages_path = self.get_packages_path()
        if not os.path.exists(packages_path):
            return []
        folders = [name for name in os.listdir(packages_path) if os.path.isdir(os.path.join(packages_path, name))]
        return folders

    def select_folder(self, folder):
        packages_path = self.get_packages_path()
        folder_path = os.path.join(packages_path, folder)
        json_file_path = os.path.join(folder_path, "Fusion.json")

        if not os.path.exists(json_file_path):
            # Create the Fusion.json file and prompt the user to select the main file
            files = os.listdir(folder_path)
            options = [[file, lambda file=file: self.set_main_file(folder_path, file)] for file in files]
            options.append(["Back", self.menu.start])
            self.menu.options = options
            print("Please select the main file:")
            time.sleep(3)
            self.menu.start()
        else:
            with open(json_file_path, "r") as file:
                try:
                    data = json.load(file)
                    main_file = data.get("main")
                    if main_file:
                        main_file_path = os.path.join(folder_path, main_file)
                        if os.path.exists(main_file_path):
                            # Change the current working directory to the folder path
                            os.chdir(folder_path)

                            # Run the main Python file in a separate process and wait for it to finish
                            execution_command = FileExecutor.get_execution_command(main_file_path, folder_path)
                            if execution_command:
                                try:
                                    process = pexpect.spawn(execution_command)
                                    process.interact()
                                except pexpect.ExceptionPexpect as e:
                                    print(f"Error executing file: {e}")
                                    time.sleep(2)
                            else:
                                print("Execution command not available.")
                                time.sleep(2)
                            
                        else:
                            print("Main Python file not found.")
                            time.sleep(2)
                    else:
                        print("No 'main' key found in Fusion.json.")
                        time.sleep(2)
                except json.JSONDecodeError:
                    print("Error parsing Fusion.json")
                    time.sleep(2)

        time.sleep(3)
        print("Press enter to get back...")
        input()
        self.menu.start()


    def set_main_file(self, folder_path, file):
        folder_path = os.path.abspath(folder_path)
        json_file_path = os.path.join(folder_path, "Fusion.json")
        data = {"main": file}
        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file)
        print(f"Main file '{file}' has been set for the package.\ngo back to the pacakges to run it")
        time.sleep(3)


    def update_menu(self):
        self.menu = Menu([], parent_menu=self.main_menu, numbered=True)  # Initialize an empty menu
        folders = self.get_folders()
        options = [[folder, lambda folder=folder: self.select_folder(folder)] for folder in folders]
        options.append(["Back", self.menu.start])
        self.menu.options = options

    def run(self):
        self.update_menu()  # Update the menu options initially
        self.menu.set_message('Run installed packages and dependencies.',color=colorama.Fore.LIGHTYELLOW_EX)
        self.menu.start()


