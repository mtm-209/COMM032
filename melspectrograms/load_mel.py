import os
import numpy as np
import matplotlib.pyplot as plt


def plot_mel(directory):
    """
    Plots the first mel spectrogram for each language and ratio combination in a 3x5 subplot.

    Args:
        directory (str): The directory containing the `mels` directory.
    """
    # Create a 3x5 subplot
    fig, axes = plt.subplots(nrows=3, ncols=5, figsize=(12, 8))
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    # Loop through each language directory
    for i, language in enumerate(sorted(os.listdir(os.path.join(directory, "mels")))):
        language_path = os.path.join(directory, "mels", language)

        # Loop through each ratio directory
        for j, ratio in enumerate(sorted(os.listdir(language_path))):
            ratio_path = os.path.join(language_path, ratio)

            # Load the first mel spectrogram for this language and ratio
            clip = sorted(os.listdir(ratio_path))[0]
            clip_path = os.path.join(ratio_path, clip)
            mel_spec = np.load(clip_path)

            # Plot the mel spectrogram on the subplot
            ax = axes[i][j]
            ax.imshow(mel_spec, origin="lower", cmap="viridis")
            ax.set_title(f"{language} - {ratio}")
            ax.axis("off")

    plt.show()


dir = r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav"
plot_mel(dir)
