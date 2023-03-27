import os
import librosa
import numpy as np
import matplotlib.pyplot as plt


def convert_wavs_to_melspecs(dir_path):
    # Define paths
    wavs_folder = os.path.join(dir_path, 'wavs')
    mels_folder = os.path.join(dir_path, 'mels')

    # Create 'mels' subfolder if it doesn't exist
    os.makedirs(mels_folder, exist_ok=True)

    # Loop over all .wav files in 'wavs' subfolder
    for filename in os.listdir(wavs_folder):
        if filename.endswith('.wav'):
            # Load audio file
            filepath = os.path.join(wavs_folder, filename)
            y, sr = librosa.load(filepath, sr=22050)

            # Create mel spectrogram
            mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=512, n_mels=128)
            mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

            # Save mel spectrogram as .npy file in 'mels' subfolder
            basename = os.path.splitext(filename)[0]
            np.save(os.path.join(mels_folder, f'{basename}.npy'), mel_spec_db)


def show_melspec(filename, dir_path):
    # Define paths
    mels_folder = os.path.join(dir_path, 'mels')
    filepath = os.path.join(mels_folder, filename)

    # Load mel spectrogram
    mel_spec_db = np.load(filepath)

    # Show mel spectrogram
    plt.figure(figsize=(10, 4))
    plt.imshow(mel_spec_db, cmap='coolwarm', origin='lower', aspect='auto')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Mel Spectrogram: {filename}')
    plt.xlabel('Time (frames)')
    plt.ylabel('Frequency (Hz)')
    plt.tight_layout()
    plt.show()


#convert_wavs_to_melspecs(r'C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav')
#show_melspec("common_voice_es_18737267.npy", r"C:\Users\matth\OneDrive\Documents\COMM032\datasets_wav")

