import os

# Define paths
input_file = 'user-config'
output_directory = 'user-config'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Read filenames from the input file
with open(input_file, 'r') as file:
    filenames = file.readlines()

# Create files in the output directory
for filename in filenames:
    # Strip any extra whitespace or newline characters
    filename = filename.strip()
    
    # Construct the full path for each new file
    file_path = os.path.join(output_directory, filename)
    
    # Create an empty file (or overwrite if it exists)
    with open(file_path, 'w') as new_file:
        pass  # This will create an empty file

print(f"Files created in {output_directory}")