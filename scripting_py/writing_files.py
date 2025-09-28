def create_scientist_list(filename):
    """Reads the file and extracts a list of AI scientist names."""
    scientist_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line by comma to extract the name part
                parts = line.split(',')
                if parts:
                    # Take the first part (name) and strip any leading/trailing whitespace
                    name = parts[0].strip()
                    scientist_list.append(name)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    return scientist_list