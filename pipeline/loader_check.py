from tensorflow_loader import create_dataset
import numpy as np

# Define data directory and batch size
data_dir = r'C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav\mels'
batch_size = 32
skew = '50-50'

# Create dataset
training_dataset = create_dataset(data_dir, skew, batch_size)  # shuffle=True)

# Inspect components of dataset
for data, labels in training_dataset.take(1).as_numpy_iterator():
    print('Data shape:', data.shape)   # Should print (32, num_mels, time_steps)
    print('Labels:', labels)   # Should print an array of 32 labels (0, 1, or 2)

# Inspect the first spectrogram in the dataset
for data, _ in training_dataset.take(1):
    print('Spectrogram:', data[0].numpy())   # Should print a NumPy array of shape (num_mels, time_steps)

for example_spectrograms, example_spect_labels in training_dataset.take(1):
  break

input_shape = example_spectrograms.shape[1:]
print('Input shape:', input_shape)
