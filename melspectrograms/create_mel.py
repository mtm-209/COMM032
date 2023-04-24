import os
import librosa
import numpy as np
from tqdm import tqdm


def convert_wav_to_mel(directory):
    """
    Converts .wav files in a directory to mel spectrograms and saves them as .npy files in a `mels` directory
    at the same level as the original `wavs` directory.

    Args:
        directory (str): The directory containing the `wavs` directory.
    """
    # Set the mels directory path
    mels_directory = os.path.join(directory, "mels")

    # Loop through each language directory
    for language in os.listdir(os.path.join(directory, "wavs")):
        language_path = os.path.join(directory, "wavs", language)

        # Loop through each ratio directory
        for ratio in os.listdir(language_path):
            ratio_path = os.path.join(language_path, ratio)

            # Loop through each clip in the clips directory
            clips_path = os.path.join(ratio_path, "clips")
            for clip in tqdm(os.listdir(clips_path), desc=f"Processing {language} - {ratio}"):
                clip_path = os.path.join(clips_path, clip)

                # Load the audio file
                y, sr = librosa.load(clip_path)

                # Convert the audio to a mel spectrogram
                mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)

                # Convert the mel spectrogram to a log mel spectrogram
                log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)

                # Save the log mel spectrogram as a .npy file
                save_path = os.path.join(mels_directory, language, ratio, clip[:-4] + ".npy")
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                np.save(save_path, log_mel_spec)


directory = r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav"
convert_wav_to_mel(directory)



