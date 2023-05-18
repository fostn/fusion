import os
import json
import time
import subprocess
from ui.menu import Menu
from blessed import Terminal
import pexpect
class Packager:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.menu = Menu([], parent_menu=self.main_menu,numbered=True)
        self.terminal = Terminal()
        self.run()

    def get_folders(self):
        current_path = os.path.join(os.getcwd(), "Packages")
        if not os.path.exists(current_path):
            return []
        folders = [name for name in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, name))]
        return folders

    def select_folder(self, folder):
        folder_path = os.path.join(os.getcwd(), "Packages", folder)
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
                            # Run the main Python file in a separate process and wait for it to finish
                            os.chdir(folder_path)
                            process = pexpect.spawn("python", [main_file_path])
                            process.interact()
                            os.chdir(os.getcwd())

                            
                        else:
                            print("Main Python file not found.")
                    else:
                        print("No 'main' key found in Fusion.json.")
                except json.JSONDecodeError:
                    print("Error parsing Fusion.json.")

        time.sleep(3)
        print("Press enter to get back...")
        input()
        self.menu.start()

    def set_main_file(self, folder_path, file):
        json_file_path = os.path.join(folder_path, "Fusion.json")
        data = {"main": file}
        with open(json_file_path, "w") as file:
            json.dump(data, file)
        print(f"Fusion.json file created with main file: {file}")

    def run(self):
        folders = self.get_folders()
        options = [[folder, lambda folder=folder: self.select_folder(folder)] for folder in folders]
        options.append(["Back", self.menu.start])
        self.menu.options = options
        self.menu.start()
