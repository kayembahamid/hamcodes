import os

# Replace 'folder_path' with the path to your folder containing the .mp4 files
folder_path = '/Users/macbook/Documents/Shorts-Content/Uploaded-Theme'


# Loop through each file in the directory
for filename in os.listdir(folder_path):
    # Check if the file is an .mp4 file by looking at its extension
    if filename.lower().endswith('.mp4'):  # This ensures the check is case-insensitive
        # Construct the new filename by adding 'Riddle' at the beginning
        new_filename = 'riddle' + filename
        # Construct the full old and new file paths
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed "{filename}" to "{new_filename}"')

print('Renaming completed.')
