# Contribution Guide

Welcome to the project! We appreciate your interest in contributing. This guide will provide you with the necessary information to contribute effectively to our project.

## Table of Contents

- [Types of Contributions](#types-of-contributions)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Making Contributions](#making-contributions)
  - [Submitting Issues](#submitting-issues)
  - [Creating Pull Requests](#creating-pull-requests)
- [Coding Guidelines](#coding-guidelines)
- [Release procedure](#release-procedure)



## Types of Contributions

There are several ways to contribute to our project:

1. **Bug Reports**: If you come across any issues or bugs, please report them using the issue tracker.
2. **Feature Requests**: If you have any ideas or suggestions for new features, please submit them as feature requests.
3. **Code Contributions**: You can contribute to the project by submitting pull requests with bug fixes, new features, or improvements.
4. **Documentation**: Help improve the project's documentation by suggesting edits, adding examples, or fixing errors.
5. **Testing**: Test the project, report any issues you encounter, and provide feedback on existing features.

## Getting Started

To get started with the project, follow these steps:

### Installation

**Installation Guide**

1. **Clone the Repository**: Start by cloning the repository containing the script to your local machine. You can use the following command in your terminal or command prompt:
```git clone <repository_url>```

2. **Install Dependencies**: The script relies on external dependencies that need to be installed. Run the following command to install the required dependencies using pip:
```pip install Office365-REST-Python-Client```

3. **Set Up Authentication**: Provide the required authentication credentials to connect to the SharePoint site. Make sure you have the necessary permissions to access and upload files to the target SharePoint document library.

4. **Configure Script Parameters**: Open the script file (e.g., `Push2Sharepoint.py`) and modify the following parameters:
- `--username`: Set the SharePoint username for authentication.
- `--password`: Set the SharePoint password for authentication.
- `--site_url`: Set the URL of the SharePoint site where the files will be uploaded.
- `--folder_name`: Set the name of the target folder in the SharePoint document library.
- `--documents`: Provide the list of documents to be uploaded. Separate multiple documents with spaces.

5. **Run the Script**: Execute the script by running the following command in your terminal or command prompt:
```python Push2Sharepoint.py```


The script will connect to the SharePoint site, create the specified folder if it doesn't exist, and upload the provided documents to the target folder.

That's it! You have successfully installed and configured the script for uploading files to SharePoint. Make sure to follow the provided guidelines and provide accurate credentials and parameters to ensure a successful execution.



## Making Contributions

### Submitting Issues

If you encounter any issues or bugs, please submit them using the issue tracker. Include detailed information about the problem, including steps to reproduce it, expected behavior, and any relevant logs or error messages.

### Creating Pull Requests

To contribute code or documentation changes:

1. Fork the repository and create a new branch for your contribution.
1. Make the necessary changes in your branch.
1. Test your changes thoroughly.
1. Submit a pull request to the main repository, clearly describing the purpose of the pull request and any relevant information or context.

We will review your pull request and provide feedback. Once approved, your changes will be merged into the main repository.

## Coding Guidelines

1. Imports: The imports are grouped at the beginning of the script, separated by empty lines. They are organized in a logical order, with standard library imports first and third-party imports next.
1. Logging: The logging module is used for setting up logging. Three basicConfig calls are made with different logging levels and formats.
1. Argument Parsing: The argparse module is used to parse command-line arguments. The ArgumentParser instance is created, and arguments are added with descriptions and required attributes.
1. Class Definition: The SharePointFileManager class is defined with its constructor and various methods. The methods are separated by empty lines for better readability.
1. Private Methods: Private methods of the class are prefixed with an underscore (_) to indicate their visibility.
1. Docstrings: Docstrings are provided for class, methods, and functions to describe their purpose and usage. The docstrings follow the recommended style of enclosing the text in triple quotes.
1. Variable Naming: Variable names are meaningful and follow the snake_case naming convention. They are descriptive and help in understanding their purpose.
1. Whitespace: Appropriate use of whitespace, such as blank lines between logical sections and indentation, improves readability.
1. Conditional Statements: The if statements are properly indented and follow the recommended style of using a space before and after the comparison operator.
1. String Formatting: f-strings are used for string interpolation, which allows variables to be directly inserted within strings for better readability.


## Release procedure

Upon creating a new release all the versions should be increased to match the version of the planned release.
The following files contain hardcoded values of the version: 
[README.md](./README.md)
[action.yml](./action.yml)




