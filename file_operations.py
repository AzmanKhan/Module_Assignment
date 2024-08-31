
def read_file(file_path):
    """Read the content of a file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, data):
    """Write data to a file, overwriting any existing content."""
    with open(file_path, 'w') as file:
        file.write(data)

def append_to_file(file_path, data):
    """Append data to a file."""
    with open(file_path, 'a') as file:
        file.write(data)
    