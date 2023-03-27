import os
import tensorflow as tf
import numpy as np

import os
import glob
import librosa
import numpy as np
import tensorflow as tf

import os
import tensorflow as tf
import numpy as np
import librosa


class CreateDataset(tf.keras.utils.Sequence):
    def __init__(self, dir_path, batch_size, skew=None):
        self.dir_path = dir_path
        self.batch_size = batch_size
        self.skew = skew

        self.labels = []
        self.filepaths = []

        self._parse_dir()

    def __len__(self):
        return int(np.ceil(len(self.filepaths) / self.batch_size))

    def __getitem__(self, idx):
        batch_filepaths = self.filepaths[idx * self.batch_size: (idx + 1) * self.batch_size]
        batch_labels = self.labels[idx * self.batch_size: (idx + 1) * self.batch_size]

        batch_data = [self._load_data(filepath) for filepath in batch_filepaths]

        return tf.convert_to_tensor(batch_data), tf.convert_to_tensor(batch_labels)

    def _parse_dir(self):
        for lang_folder in os.listdir(self.dir_path):
            if lang_folder not in ['en', 'es', 'pl']:
                continue

            lang_path = os.path.join(self.dir_path, lang_folder)

            for abc_folder in os.listdir(lang_path):
                abc_path = os.path.join(lang_path, abc_folder)

                if self.skew and not abc_path.endswith(self.skew):
                    continue

                for filepath in os.listdir(abc_path):
                    if filepath.endswith('.npy'):
                        self.labels.append(lang_folder)
                        self.filepaths.append(os.path.join(abc_path, filepath))

    def _load_data(self, filepath):
        data = np.load(filepath)
        return data


# Define data directory and batch size
#data_dir = r'C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav\mels'
#batch_size = 1
#skew = '50-50'
# Create dataset
#dataset = CreateDataset(data_dir, batch_size, skew)#shuffle=True)

# Inspect components of dataset
