from ui.menu import Menu
from download.downloader import Downloader
from Packages.packager import Packager
from Packages.Deleter import Deleter
import colorama
import pkg_resources
import json

class Fusion:
    def __init__(self):
        version = pkg_resources.require("fusion")[0].version
        logo = f"""
       ______           _                
      / ____/_  _______(_)___  ____      
     / /_  / / / / ___/ / __ \/ __ \     
    / __/ / /_/ (__  ) / /_/ / / / /     
   /_/    \__,_/____/_/\____/_/ /_/      
        powered by f09l
        version {version}                               
        """                        

        main_menu = Menu([
            ["Downloader", lambda: Downloader(main_menu=main_menu)],
            ["Packages", lambda: Packager(main_menu=main_menu)],
            ["Delete Package",lambda: Deleter(main_menu=main_menu)],
            ["Exit", lambda: exit()]
        ], logo=logo)

      
        main_menu.set_message( "Welcome to Fusion! Please make a selection.")
       
        main_menu.start()


if __name__ == "__main__":
    Fusion()
