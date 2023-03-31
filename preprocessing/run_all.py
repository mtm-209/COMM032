import os
from create_skew import *
from create_dir import create_subfolders
from read_tar import create_tsv, copy_clips_folder


def process_folder(target_dir, output_dir, skew):
    create_subfolders(target_dir, output_dir, skew)

    for filename in os.listdir(target_dir):
        if filename.endswith(".tar.gz"):
            dir_name = filename.replace(".tar.gz", "").split("-")[-1]
        elif filename.endswith(".tar"):
            dir_name = filename.replace(".tar", "").split("-")[-1]

        for s in skew:
            output_path = os.path.join(output_dir, dir_name, s)
            create_tsv(os.path.join(target_dir, filename), output_path, s)
            copy_clips_folder(os.path.join(target_dir, filename), output_path, s, True)


# Only use these
datasets = r"C:\Users\matth\OneDrive\Documents\COMM032\datasets"
datasets_zipped = r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_zipped"
skews_lst = ["10-90","25-75", "50-50", "75-25", "90-10"]

# Run
process_folder(datasets_zipped, datasets, skews_lst)
# port_file = r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_zipped\cv-corpus-10.0-delta-2022-07-04-pt.tar.gz"
