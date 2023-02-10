import os


def extract_and_create_dir(input_dir, target_dir):
    """
    Take the unique marker of the filename and create 
    a folder for each one. 
    """
    for filename in os.listdir(input_dir):
        if filename.endswith(".tar.gz"):
            dir_name = filename.replace(".tar.gz", "").rsplit("-", 1)[-1]
            dir_path = os.path.join(target_dir, dir_name)
            os.makedirs(dir_path, exist_ok=True),


def get_dir_names_only(input_dir):
    dir_names = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".tar.gz"):
            dir_name = filename.replace(".tar.gz", "").rsplit("-", 1)[-1]
            dir_names.append(dir_name)
    return dir_names


def create_subfolders(input_dir, target_dir, subfolder_names):
    """
    Create a subfolder for each skew.
    """
    extract_and_create_dir(input_dir, target_dir)  # Call the function to create a folder for each language

    for folder in os.listdir(target_dir):
        folder_path = os.path.join(target_dir, folder)
        if os.path.isdir(folder_path):
            for subfolder_name in subfolder_names:
                subfolder_path = os.path.join(folder_path, subfolder_name)
                os.makedirs(subfolder_path, exist_ok=True)

