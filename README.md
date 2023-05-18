# Fusion

Fusion is a command-line tool designed to simplify the management and execution of Python projects. It provides a user-friendly interface for organizing files, running scripts, managing dependencies, and facilitating seamless interactions with the command line.

## Features

- **Package Management:** Fusion allows you to organize your Python projects into packages, making it easier to manage different components and files associated with your project.
- **Menu System:** Fusion provides a menu-driven system that enables users to navigate through different options and perform various actions. It allows you to select and run specific files or scripts within a package.
- **Execution of Python Files:** Fusion allows you to execute the main Python files within your packages. It automatically detects the main file specified in a Fusion.json configuration file or prompts you to select the main file if it's not defined.
- **Interactive Input:** Fusion supports interactive input, allowing users to enter input values and interact with the executed Python files directly from the command line.
- **Seamless Integration:** Fusion seamlessly integrates with the command line environment, providing a clean and user-friendly interface for improved productivity.
- **Download System:** Fusion includes a download system that allows you to retrieve files from remote sources. You can specify a URL and destination path to download files directly from the internet, making it convenient to fetch resources or dependencies for your projects.

## Installation

To install and use Fusion, follow these steps:

1 Clone the Fusion repository to your local machine:

```
git clone https://github.com/fostn/fusion
```
2 Navigate to the Fusion project directory:
```
cd fusion
```
3 Install the required dependencies:
```
pip install .
```
## Usage
To run Fusion, use the following command:
```
fusion
```

Once you have launched Fusion, you can use the menu system to navigate through different options and perform actions. The main menu allows you to select packages, execute Python files, manage dependencies, and access other functionalities provided by Fusion.

## Package Management
Select a package to explore its contents and execute files within the package.

# Execution of Python Files
If a package contains a Fusion.json file with a specified main file, Fusion will automatically execute that file. Otherwise, it will prompt you to select the main file from the available options.

# Interactive Input
When executing a Python file, Fusion supports interactive input. You can enter values and interact with the script directly from the command line.

# Download System
Fusion provides a download system that allows you to retrieve files from remote sources. You can specify a URL and destination path to download files directly from the internet.

# Contributing
Contributions to Fusion are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. See CONTRIBUTING.md for more information on how to contribute to the project.

# License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as per the terms of the license.

Acknowledgments
The Fusion tool was developed to simplify Python project management and execution.

Special thanks to the open-source community for their contributions and support.
