import numpy as np
import pandas as pd
import sklearn
from scipy import signal
from scipy.io import wavfile
import librosa
import librosa.display
import os
import matplotlib.pyplot as plt
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp


def create_labels(input_dir):  # , skew):
    labels = []
    for i in os.listdir(input_dir):
        labels.append(i)

    return labels


datasets = r"C:\Users\matth\OneDrive\Documents\COMM032\datasets"


# print(create_labels(datasets))

def create_melspectrogram(input_dir, skew):
    lan = 'pt'
    clip_folder = 'clips'
    folder_path = os.path.join(input_dir, lan, skew, clip_folder)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)



#create_melspectrogram(datasets, skew='50-50')
def create_mel(input_dir, lan, skew):
    clips_folder = 'clips'
    for l in lan:
        for s in skew:
            path = os.path.join(input_dir, l, s, clips_folder)
            for file in os.listdir(path):
                return None


####create_mel(datasets, create_labels(datasets), skew = ['25-75', '50-50', '75-25'])


def create_wav(input_dir, skew):
    lan = 'pt'
    clips_folder = 'clips'
    folder_path = os.path.join(input_dir, lan, skew, clips_folder)
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp3'):
            mp3_file_path = os.path.join(folder_path, filename)
            audio = AudioSegment.from_mp3(mp3_file_path)
            # Save the audio to wav format and remove the original mp3 file
            file_name_without_extension = os.path.splitext(filename)[0]
            wav_file_path = os.path.join(folder_path, file_name_without_extension + ".wav")
            audio.export(wav_file_path, format="wav")
            os.remove(mp3_file_path)

create_wav(datasets, skew='50-50')