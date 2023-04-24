import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define the batch size and image dimensions
batch_size = 32
img_height = 128
img_width = 128
num_classes = 3

# Define the directory for the data
data_dir = r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav\mels_flipped\50-50"

# create a list to hold the labels
labels = ['en', 'de', 'pt']

# create an empty list to hold all the melspectograms
melspectograms = []

# loop through each label
for label in labels:
    # set the path to the label directory
    label_path = os.path.join(data_dir, label)
    # loop through each .npy file in the label directory
    for filename in os.listdir(label_path):
        if filename.endswith('.npy'):
            # load the melspectogram from the .npy file
            with open(os.path.join(label_path, filename), 'rb') as f:
                melspectogram = np.load(f)
            # add the melspectogram and label to the list
            melspectograms.append((melspectogram, label))

# shuffle the list of melspectograms
np.random.shuffle(melspectograms)

# create a dataset from the list of melspectograms
ds = tf.data.Dataset.from_generator(
    lambda: ((melspectogram, label) for melspectogram, label in melspectograms),
    output_types=(tf.float32, tf.string),
    output_shapes=((128, 128, 3), ())
)

# print the dataset
for element in ds.take(10):
    print(element)

