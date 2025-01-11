import os
import py_compile

def check_files(directory):
    """
    Check for empty and corrupted Python files in the specified directory.

    Args:
        directory (str): The path to the directory to check.

    Returns:
        tuple: A tuple containing two lists:
            - empty_files: List of paths to empty Python files.
            - corrupted_files: List of paths to corrupted or problematic Python files.
    """
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return [], []

    empty_files = []
    corrupted_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):  # Check if the file has .py extension
                file_path = os.path.join(root, file)
                try:
                    if os.path.getsize(file_path) == 0:
                        print(f"Empty Python file: {file_path}")
                        empty_files.append(file_path)
                    else:
                        # Check if the file is corrupted or has syntax errors
                        py_compile.compile(file_path, doraise=True)
                        print(f"Valid Python file: {file_path}")
                except (SyntaxError, FileNotFoundError, IOError):
                    print(f"Corrupted or problematic Python file: {file_path}")
                    corrupted_files.append(file_path)

    return empty_files, corrupted_files

# Specify the project path
project_path = os.path.join("/Users", "michelegrimaldi", "Desktop", "Chatbot_SoundBot", "ChatBot")

# Check the files
empty_files, corrupted_files = check_files(project_path)

# Print the results
if empty_files:
    print("\nEmpty Python files found:")
    for file in empty_files:
        print(file)
else:
    print("\nNo empty Python files found.")

if corrupted_files:
    print("\nCorrupted or problematic Python files found:")
    for file in corrupted_files:
        print(file)
else:
    print("\nNo corrupted Python files found.")