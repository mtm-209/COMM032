from create_skew import *
import os
import tarfile
from tqdm import tqdm


def get_val_from_tar(file_path, skew, max_samples):
    filename = os.path.basename(file_path)
    mode = "r:gz" if os.path.splitext(filename)[1] == ".gz" else "r"
    with tarfile.open(file_path, mode) as tar:
        member = next((m for m in tar.getmembers() if os.path.basename(m.name) == "validated.tsv"), None)
        if member:
            file = tar.extractfile(member)
            val_lst, val_df = target_data(file, skew, max_samples)
            return val_lst, val_df


def create_tsv(file_path, output_path, skew, max_samples):
    """
    This creates a csv for your filtered dataframe.
    ---------
    Params:
    df (DataFrame): Input DataFrame
    file_name (str):
    """
    df = get_val_from_tar(file_path, skew, max_samples)[1]
    path = output_path + '/validated.tsv'
    return df.to_csv(path, sep="\t")


def copy_clips_folder(src, dst, skew, max_samples, delete=False, ):
    filename = os.path.basename(src)
    mode = "r:gz" if os.path.splitext(filename)[1] == ".gz" else "r"
    with tarfile.open(src, mode) as tar:
        clips_folder = None
        for member in tar.getmembers():
            if '/clips/' in member.name:
                clips_folder = os.path.dirname(member.name)
                break

        if not clips_folder:
            print("No 'clips' folder found in tar file")
            return

        desired_files = get_val_from_tar(src, skew, max_samples)[0]
        members_to_extract = []

        for member in tqdm(tar.getmembers()):
            if member.name.startswith(clips_folder) and os.path.basename(member.name) in desired_files:
                member.name = os.path.join(dst, 'clips', os.path.basename(member.name))
                members_to_extract.append(member)

        tar.extractall(path=dst, members=members_to_extract)

        if delete:
            # delete original files
            for filename in desired_files:
                src_file = os.path.join(dst, clips_folder, filename)
                if os.path.exists(src_file):
                    os.remove(src_file)

