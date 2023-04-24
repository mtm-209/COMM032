import os
import shutil
from tqdm import tqdm


def flip_directory_order(input_dir):
    # create a new directory to store the flipped directory structure
    output_dir = input_dir + "_flipped"
    os.makedirs(output_dir, exist_ok=True)

    # iterate over all the language directories
    for lang_dir in tqdm(os.listdir(input_dir), desc="Flipping directory"):
        # iterate over all the skew directories for this language
        for skew_dir in os.listdir(os.path.join(input_dir, lang_dir)):
            # create the new directories if they don't exist yet
            output_lang_dir = os.path.join(output_dir, skew_dir)
            output_skew_dir = os.path.join(output_lang_dir, lang_dir)
            os.makedirs(output_skew_dir, exist_ok=True)

            # copy all the files from the input directory to the output directory
            input_skew_dir = os.path.join(input_dir, lang_dir, skew_dir)
            for filename in os.listdir(input_skew_dir):
                input_path = os.path.join(input_skew_dir, filename)
                output_path = os.path.join(output_skew_dir, filename)
                shutil.copyfile(input_path, output_path)

    return output_dir


def flatten_directory(input_dir):
    # iterate over all the directories at the pentultimate layer
    for root, dirs, files in os.walk(input_dir):
        for dir_name in dirs:
            # check if there is a "clips" directory inside this directory
            clips_dir = os.path.join(root, dir_name, "clips")
            if os.path.isdir(clips_dir):
                # move all the files from the clips directory to the parent directory
                for filename in os.listdir(clips_dir):
                    src_path = os.path.join(clips_dir, filename)
                    dst_path = os.path.join(root, dir_name, filename)
                    shutil.move(src_path, dst_path)

                # remove the clips directory
                os.rmdir(clips_dir)

    return input_dir


#flattened_dir = flatten_directory(r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav\wavs")
flipped_dir = flip_directory_order(r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_new")
