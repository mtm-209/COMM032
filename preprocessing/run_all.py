import os
from create_skew import *
from create_dir import create_subfolders
from read_tar import create_tsv, copy_clips_folder
from dir_flipper import flip_directory_order, flatten_directory


def process_folder(target_dir, output_dir, skew, max_samples):
    create_subfolders(target_dir, output_dir, skew)

    for filename in os.listdir(target_dir):
        if filename.endswith(".tar.gz"):
            dir_name = filename.replace(".tar.gz", "").split("-")[-1]
        elif filename.endswith(".tar"):
            dir_name = filename.replace(".tar", "").split("-")[-1]

        for s in skew:
            output_path = os.path.join(output_dir, dir_name, s)
            create_tsv(os.path.join(target_dir, filename), output_path, s, max_samples)
            copy_clips_folder(os.path.join(target_dir, filename), output_path, s, max_samples, True)


# Only use these
datasets = r"C:\Users\matth\OneDrive\Documents\COMM032\demo_dataset"
datasets_zipped = r"C:\Users\matth\OneDrive\Documents\COMM032\demo_zipped"
skews_lst = ["10-90","25-75", "50-50", "75-25", "90-10"]
max_samples = 500  # Change for demo

# Run
process_folder(datasets_zipped, datasets, skews_lst, max_samples)
flattened_dir = flatten_directory(datasets)
flipped_dir = flip_directory_order(datasets)
