import os
from ui.menu import Menu
import time
import colorama
class Deleter:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.menu = Menu([
            ["Delete Package", self.delete_package],
            ["Back", self.main_menu.start]
        ], main_menu=self.main_menu)
        self.menu.set_message("This action will permanently remove the package and its associated files",color=colorama.Fore.LIGHTRED_EX)
        self.menu.start()
        #self.delete_package()
    def delete_package(self):
        print("Packages available for deletion:")
        time.sleep(2)
        packages = self.get_package_list()
        for package in packages:
            print(package)

        package_name = self.menu.get_input("Enter the name of the package to delete: ")
        package_directory = os.path.join("Packages", package_name)

        # Check if the package directory exists
        if not os.path.exists(package_directory):
            print(f"The package '{package_name}' does not exist.")
            time.sleep(2)
            self.menu.start()
            return
        if not package_name:
            print("Deletion cancelled.")
            time.sleep(2)
            self.menu.start()
            return
        if package_name not in packages:
            print(f"The package '{package_name}' does not exist.")
            time.sleep(2)
            self.menu.start()
            return
        confirm = self.menu.get_input(f"Are you sure you want to delete the package '{package_name}'? (y/n) ")
        if confirm.lower() == "y":
            self.delete_directory(package_directory)
            print(f"The package '{package_name}' has been deleted.")
            time.sleep(2)
        else:
            print("Deletion cancelled.")
            time.sleep(2)
        self.menu.start()


    def get_package_list(self):
        packages = []
        for item in os.listdir("Packages"):
            if os.path.isdir(os.path.join("Packages", item)):
                packages.append(item)
        return packages

    def delete_directory(self, directory):
        for root, dirs, files in os.walk(directory, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)
        os.rmdir(directory)
