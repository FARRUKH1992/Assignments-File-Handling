import os

def list_directory_contents(path):
    try:
        # Check if the provided path exists
        if os.path.exists(path):
            # List and print all files and subdirectories in the given path
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    print(f"[Directory] {full_path}")
                else:
                    print(f"[File] {full_path}")
        else:
            print(f"Error: The path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main block to run the function
if __name__ == "__main__":
    # Prompt the user for a directory path
    directory_path = input("Enter the directory path to inspect: ")
    # Call the function to list the directory contents
    list_directory_contents(directory_path)
