from create_skew import *
import os
import tarfile
from tqdm import tqdm


def get_val_from_tar(file_path, skew):  # destination_dir):
    with tarfile.open(file_path, "r:gz") as tar:
        for member in tqdm(tar.getmembers()):
            if "/validated.tsv" in member.name:
                file = tar.extractfile(member)
                val_lst, val_df = target_data(file, skew)
                # print(member)#val_lst
                return val_lst, val_df


def create_tsv(file_path, output_path, skew):
    """
    This creates a csv for your filtered dataframe.
    ---------
    Params:
    df (DataFrame): Input DataFrame
    file_name (str):
    """
    df = get_val_from_tar(file_path, skew)[1]
    path = output_path + '/validated.tsv'
    return df.to_csv(path, sep="\t")


def copy_clips_folder(src, dst, skew):
    with tarfile.open(src, "r:gz") as tar:
        clips_folder = None
        for member in tar.getmembers():
            if '/clips/' in member.name:
                clips_folder = os.path.dirname(member.name)
                break

        if not clips_folder:
            print("No 'clips' folder found in tar file")
            return

        desired_files = get_val_from_tar(src, skew)[0]
        members_to_extract = []

        for member in tqdm(tar.getmembers()):
            if member.name.startswith(clips_folder) and os.path.basename(member.name) in desired_files:
                member.name = os.path.join(dst, 'clips', os.path.basename(member.name))
                members_to_extract.append(member)

        tar.extractall(path=dst, members=members_to_extract)
