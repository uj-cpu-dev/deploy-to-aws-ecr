import os

def list_files(directory):
    try:
        # List all entries in the directory
        entries = os.listdir(directory)
        # Filter out directories, keeping only files
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        # Print the list of files
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the directory you want to list
    # For the current directory, use '.'
    directory_to_list = '.'
    list_files(directory_to_list)