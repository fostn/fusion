from blessed import Terminal
from colorama import Fore, Style,Back
import time
class Menu:
    def __init__(self, options,logo="",parent_menu=None,main_menu=None,numbered=False):
        self.term = Terminal()
        self.options = options
        self.selection = 0
        self.logo = logo
        self.parent_menu = parent_menu
        self.main_menu = main_menu
        self.numbered = numbered
    def create_gradient_logo(self):
        gradient_logo = ""
        gradient_step = 255 // (len(self.logo.splitlines()) - 1)
        for i, line in enumerate(self.logo.splitlines()):
            color = f"\033[38;2;255;{255 - (gradient_step * i)};0m"
            gradient_logo += f"{color}{line}{Style.RESET_ALL}\n"
        return gradient_logo

    def display_screen(self):
        print(self.term.clear())
        gradient_logo = self.create_gradient_logo()
        print(gradient_logo)

        for idx, item in enumerate(self.options):
            if self.numbered:
                number = f"{idx + 1} "
                if idx == self.selection:
                    print(self.term.reverse(f'{self.term.bold_green}{number}{item[0]:<5}'))
                else:
                    print(f'{self.term.normal}{number}{item[0]:<15}')
            else:
                if idx == self.selection:
                    print(self.term.reverse(f'{self.term.bold_green}{item[0]:<5}'))
                else:
                    print(f'{self.term.normal}{item[0]:<15}')
    def run_selection(self):
        action = self.options[self.selection][2]
        if action:
            self.display_screen()

            with self.term.fullscreen(), self.term.cbreak():
                action()
            



    def handle_input(self, key):
        if key.is_sequence:
            if key.name == 'KEY_DOWN':
                self.selection = (self.selection + 1) % len(self.options)
            elif key.name == 'KEY_UP':
                self.selection = (self.selection - 1) % len(self.options)
            elif key.name == 'KEY_ENTER':
                if self.selection == len(self.options) - 1:  # Exit option
                    self.handle_exit()
                else:
                    action = self.options[self.selection][1]
                    if action:
                        self.display_screen()
                        with self.term.fullscreen(), self.term.cbreak():
                            action()
                        self.display_screen()  # Redraw menu after action
        elif key:
            print(f"Got {key}.")
            self.display_screen()

    def handle_exit(self):
        if self.parent_menu:
            self.parent_menu.start()
        else:
            try:
                self.main_menu.start()
            except:
                exit()


    def get_input(self, prompt):
        with self.term.cbreak():
            print(prompt, end="", flush=True)
            input_text = ""
            while True:
                key = self.term.inkey()
                if key.is_sequence:
                    if key.name == "KEY_ENTER":
                        print()
                        break
                    elif key.name == "KEY_BACKSPACE":
                        if len(input_text) > 0:
                            input_text = input_text[:-1]
                            print("\b \b", end="", flush=True)
                    else:
                        input_text += key
                        print(key, end="", flush=True)
                elif key:
                    input_text += key
                    print(key, end="", flush=True)

            return input_text

    def start(self):
        with self.term.fullscreen(), self.term.cbreak():
            while True:
                self.display_screen()
                key = self.term.inkey()
                self.handle_input(key)
                