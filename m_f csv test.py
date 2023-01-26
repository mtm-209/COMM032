import numpy as np
import pandas as pd 
import csv 
import google 
#from google.colab import drive  # Mount the google drive so that it can be accessed
#drive.mount('/content/drive')
import os 
import pathlib 
import tqdm
import codecs

data_dir = r'G:\My Drive\common_voice_kpd\English\test.csv'  # From the google drive create a directory
data_dir = pathlib.Path(data_dir)  # Create the path for the directory
data_dir


csv = r"G:\My Drive\common_voice_kpd\English\test.csv"  # From the google drive create a path to csv
def return_row_by_values(df, col, values):
    return df[df[col].isin(values)]

def target_lst(path):
    """
    This function goes throught the target csv file. 
    It then returns a list of client ids that are gendered. 

    ------
    To add:
    - Need to add way to create defined splits in the function 
      for example if we want 50:50 m, f or 75:25 etc. 
    - Want the spilts to be random 
    - Way to turn the lst into a saveable csv file. 
    - Method in which to add a random seed to repeat tests.
    - Optimise for scalability
    ------

    Params:
    path: path to the csv file.

    Returns: 
    lst: list of the client_ids to be used later. 

    """
    df = pd.read_csv(path, encoding='utf-16', delimiter = '\t')
    df = df[['client_id','gender']]
    df = return_row_by_values(df, 'gender', ['male', 'female'])
    lst = df['client_id'].to_list()
    return lst


def target_with_random(path):
    df = pd.read_csv(path, encoding='utf-16', delimiter = '\t')
    df = df[['client_id','gender']]
    df = return_row_by_values(df, 'gender', ['male', 'female'])
    #lst = df['client_id'].to_list()
    return df#lst
train_path = r"G:\My Drive\common_voice_kpd\English\train.csv"  # From the google drive create a path to csv

df = target_with_random(path = train_path)
print(df['gender'].value_counts())
