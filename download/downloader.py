from blessed import Terminal
import os
import time
import requests
from ui.menu import Menu

class Downloader:
    def __init__(self, main_menu):
          self.main_menu = main_menu
          self.menu = Menu([
            ["Download Repository", self.select_repository],
            ["Back", self.exit_action]
        ], main_menu=self.main_menu)
          self.menu.start()

    def select_repository(self):
        username = self.menu.get_input("Enter the GitHub username: ")
        api_url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(api_url)
        if response.status_code == 200:
            repositories = response.json()
            options = [[repo["name"], lambda repo=repo: self.download_repository(repo["html_url"])] for repo in repositories]
            options.append(["Back", self.menu.start])
            repo_menu = Menu(options, parent_menu=self.menu)
            repo_menu.start()
        else:
            print(f"Failed to fetch repositories for '{username}'.")
            time.sleep(3)
            self.menu.start()

    def download_repository(self, url):
        username, repo_name = url.split("/")[-2:]
        api_url = f"https://api.github.com/repos/{username}/{repo_name}/contents"
        print(f"Downloading '{repo_name}'")
        response = requests.get(api_url)
        if response.status_code == 200:
            contents = response.json()
            repo_directory = os.path.join("Packages", repo_name)
            os.makedirs(repo_directory, exist_ok=True)

            for item in contents:
                if item["type"] == "file":
                    file_path = item["path"]
                    file_url = item["download_url"]
                    save_path = os.path.join(repo_directory, file_path)

                    os.makedirs(os.path.dirname(save_path), exist_ok=True)

                    self.download_file(file_url, save_path)

            print(f"Repository '{repo_name}' downloaded.")
        else:
            print(f"Failed to fetch repository contents for '{repo_name}'.")

        time.sleep(5)

    def download_file(self, file_url, save_path):
        response = requests.get(file_url)
        response.raise_for_status()

        with open(save_path, "wb") as file:
            file.write(response.content)

    def exit_action(self):
        self.main_menu.start()

