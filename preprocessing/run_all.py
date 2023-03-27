import os
from create_skew import *
from create_dir import create_subfolders
from read_tar import create_tsv, copy_clips_folder


def process_folder(target_dir, output_dir, skew):
    create_subfolders(target_dir, output_dir, skew)

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        folder_one = filename.replace(".tar.gz", "").rsplit("-", 1)[-1]
        for s in skew:
            output_path = os.path.join(output_dir, folder_one, s)
            create_tsv(file_path, output_path, s)
            copy_clips_folder(file_path, output_path, s)


# Only use these
datasets = r"C:\Users\matth\OneDrive\Documents\COMM032\datatest"
datasets_zipped = r"C:\Users\matth\OneDrive\Documents\COMM032\datatest_zipped"
skews_lst = ["10-90", "50-50", "90-10"]

# Run
process_folder(datasets_zipped, datasets, skews_lst)
# port_file = r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_zipped\cv-corpus-10.0-delta-2022-07-04-pt.tar.gz"
