import os
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader
import pandas as pd
#from torchvision.io import read_image
import matplotlib.pyplot as plt

import os
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

class MelSpectrogramDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.labels = []
        self.filepaths = []

        # Loop over all nested a, b, and c folders
        for lang_dir in os.listdir(self.data_dir):
            if lang_dir.startswith('.'):
                continue

            # Get label based on directory name
            if lang_dir == 'en':
                label = 'en'
            elif lang_dir == 'es':
                label = 'es'
            elif lang_dir == 'pl':
                label = 'pl'
            else:
                continue

            for nested_dir in os.listdir(os.path.join(self.data_dir, lang_dir)):
                if nested_dir.startswith('.'):
                    continue

                nested_dir_path = os.path.join(self.data_dir, lang_dir, nested_dir)

                # Loop over all .npy files in nested folder
                for filename in os.listdir(nested_dir_path):
                    if filename.endswith('.npy'):
                        # Append label and filepath
                        self.labels.append(label)
                        self.filepaths.append(os.path.join(nested_dir_path, filename))

        # Define label-to-index mapping
        self.label_to_idx = {label: idx for idx, label in enumerate(sorted(set(self.labels)))}

    def __len__(self):
        return len(self.filepaths)

    def __getitem__(self, idx):
        # Load mel spectrogram and corresponding label
        mel_spec_db = np.load(self.filepaths[idx])
        label = self.label_to_idx[self.labels[idx]]

        # Convert mel spectrogram to tensor
        mel_spec_tensor = torch.FloatTensor(mel_spec_db).unsqueeze(0)

        return mel_spec_tensor, label

# Define data directory and batch size
data_dir = r'C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav\mels'
batch_size = 1

# Create dataset and dataloader
dataset = MelSpectrogramDataset(data_dir)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)


train_features, train_labels = next(iter(dataloader))
print(f"Feature batch shape: {train_features.size()}")
print(f"Labels batch shape: {train_labels.size()}")
img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap="gray")
plt.show()
print(f"Label: {label}")