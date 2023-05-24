from ui.menu import Menu
import os
import time
from .FileExecutor import FileExecutor
import json
from colorama import Fore
class Packager:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.menu = None
        self.packages_path = self.get_packages_path()
        self.start()

    def get_packages_path(self):
        current_dir = os.getcwd()
        return os.path.join(current_dir, "Packages")

    def get_folders(self):
        folders = []
        for item in os.listdir(self.packages_path):
            item_path = os.path.join(self.packages_path, item)
            if os.path.isdir(item_path):
                folders.append(item)
        return folders

    def select_folder(self, folder):
        folder_path = os.path.join(self.packages_path, folder)
        self.menu.set_message(f"Folder Path: {folder_path}")
        self.menu.clear_message()

        # Check if Fusion.json exists in the selected folder
        fusion_json_path = os.path.join(folder_path, "Fusion.json")
        if os.path.isfile(fusion_json_path):
            with open(fusion_json_path, "r") as f:
                fusion_config = json.load(f)
            main_file = fusion_config.get("main")

            if main_file:
                main_file_path = os.path.join(folder_path, main_file)

                # Execute the main file using FileExecutor
                executor = FileExecutor()
                execution_command = executor.get_execution_command(main_file_path, folder_path)
                if execution_command:
                    os.system(execution_command)
                    time.sleep(3)
                else:
                    self.menu.set_message("Invalid file extension.", color=Fore.LIGHTRED_EX)
            else:
                self.menu.set_message("No main file specified in Fusion.json.", color=Fore.LIGHTRED_EX)
        else:
            self.menu.clear_message()
            options = [[f, lambda f=f: self.select_main_file(f, folder_path)] for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            options.append(["Back", self.update_menu])
            self.menu = Menu(options, parent_menu=self.main_menu)
            self.menu.set_message("Fusion.json not found. Select a main file:",color=Fore.LIGHTRED_EX)
            self.menu.start()

    def select_main_file(self, main_file, folder_path):
        # Update Fusion.json with the selected main file
        fusion_json_path = os.path.join(folder_path, "Fusion.json")
        fusion_config = {"main": main_file}
        with open(fusion_json_path, "w") as f:
            json.dump(fusion_config, f)

        # Execute the main file using FileExecutor
        main_file_path = os.path.join(folder_path, main_file)
        executor = FileExecutor()
        execution_command = executor.get_execution_command(main_file_path, folder_path)
        if execution_command:
            os.system(execution_command)
        else:
            self.menu.set_message("Invalid file extension.", color="red")

        time.sleep(3)
        self.menu.start()
    def update_menu(self):
        folders = self.get_folders()
        options = [[folder, lambda folder=folder: self.select_folder(folder)] for folder in folders]
        options.append(["Back", self.main_menu.start])
        self.menu = Menu(options, parent_menu=self.main_menu,numbered=True)
        self.menu.start()

    def start(self):
        self.update_menu()
