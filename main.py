import sys
import os

def read_and_print_file(filename):
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1) # Exit with an error code

    try:
        # Open the file and print its content
        with open(filename, 'r') as f:
            content = f.read()
            print(f"--- Content of {filename} ---")
            print(content)
            print("---------------------------------")
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if a file path argument was provided
    if len(sys.argv) < 2:
        print("USAGE: <program> <commands_file>")
        sys.exit(1)

    # The file path is the first argument after the script name
    file_path = sys.argv[1]
    read_and_print_file(file_path)
