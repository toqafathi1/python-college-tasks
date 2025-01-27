
import os
import shutil

# define the target directroy
target_directory = r"E:\project"

# Mapping of files types to subdirectories
file_types = {
    ".pdf": "Documnets",
    ".csv": "csv-files",
    ".zip": "zip-files",
    ".ipynb": "jupyter-files",
    ".rar": "zip-files",
    ".py": "jupyter-files",
}


# loop through files in the target directory to creat full-path

for filename in os.listdir(target_directory):
    file_path = os.path.join(target_directory, filename)

    # check if the item is file
    if os.path.isfile(file_path):

        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Organize files into subdirectories
        if file_extension in file_types:
            # creat the subdirectories if it doesn't exist
            destination_directory = os.path.join(
                target_directory, file_types[file_extension])
            os.makedirs(destination_directory, exist_ok=True)

            # move the file to the corresponding subdirectory
            shutil.move(file_path, os.path.join(
                destination_directory, filename))
print("file orgnization complete.")
