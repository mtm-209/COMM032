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
import shutil

def return_row_by_values(df, col, values):
    return df[df[col].isin(values)]

# Test at 50:50 
def skew_calc(df, col, skew):
    m_count, f_count = df[col].value_counts()
    if skew == '50:50':
        value = int(m_count-f_count)
        return df[df[col].eq('male')].sample(n = (value))
    if skew == '25:75':
        val = int(m_count-(f_count/3))
        return df[df[col].eq('male')].sample(n = (val))
    if skew == '75:25':
        if (3*f_count) <= m_count:
            val = int(m_count - (f_count*3))  
            return df[df[col].eq('male')].sample(n = (val))
        else:
            val = int(f_count - (m_count/3))
            return df[df[col].eq('female')].sample(n = (val))
    else:
        return print("That is not a valid skew, please choose: '50:50', '25:75' or '75:25'")

def skew_dataset(df, col, skew):
    df = df.drop(skew_calc(df, col, skew).index)
    return df

def target_data(path, skew):
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
    # Dataframe filtering
    df = pd.read_csv(path)#, encoding='utf-16', delimiter = '\t')
    df = df[['filename','gender']]
    df = return_row_by_values(df, 'gender', ['male', 'female'])
    df = skew_dataset(df, 'gender', skew)

    # Create a list
    lst = df['filename'].to_list()
    return df , lst

test_path = r"C:\Users\matth\OneDrive\Documents\COMM032\cv-valid-test.csv"
test_2 = r"C:\Users\matth\OneDrive\Documents\COMM032\cv-valid-train.csv"

#df, lst = target_data(test_path, '50:50')
#print(lst)

def keep_string_from_column(df, column_name):
    """
    Changes the column string to only return the sample part.
    """
    df[column_name] = df[column_name].apply(lambda x: x.split("/")[-1])
    return df

def create_csv(df, file_name):
    """
    This creates a csv for your filtered dataframe.

    """
    csv = df.to_csv(file_name, index = False)
    print(f"Successfully created {file_name}")

#df, _ = target_data(test_path, '50:50')
#df = keep_string_from_column(df, 'filename')
#create_csv(df, 'test_file.csv')

def to_txt(lst, file_name):
    """
    This function return a text file of the filtered list. 
    """
    txt = lst.to_txt(file_name)
    return None  # Change for testing

def output_file(target_file, output_path):
    """
    This functions goes through the target folder. 
    Checks if they align with the txt file. 
    Then places the file in a new directory. 
    
    Named: language/skew/data/gender/file.wav
    For example we would get:
    english/50-50/train/male/00001.wav
    """
    return None

def copy_files(folder_path, csv_file, language, skew, data, gender):
    """
    ---------------
    THIS FUNCTION NEEDS DEBUGGING DO NOT RUN
    ----------------
    """
    # Open the CSV file and read the contents
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        csv_contents = list(csv_reader)

    # Create the subfolders
    subfolder_path = os.path.join(folder_path, language, skew, data, gender)
    os.makedirs(subfolder_path, exist_ok=True)

    # Iterate through all the files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is in the CSV
        if filename in [row[0] for row in csv_contents]:
            # Copy the file to the subfolder
            file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(subfolder_path, filename)
            shutil.copy2(file_path, new_file_path)

#copy_files(r"C:\Users\matth\OneDrive\Documents\COMM032\cv-valid-test", r"C:\Users\matth\OneDrive\Documents\GitHub\COMM032\test_file.csv", "English", "50-50", "test", "male")

#m_count, f_count = df['gender'].value_counts()
#print(m_count, f_count, "This is the count before")

#df = skew_dataset(df, 'gender', '75:25')
#print("This is the count after", df['gender'].value_counts(normalize = True))

# Test for 75:25
#print(int(f_count - (m_count/3)))
#print(m_count-f_count*3)
#df = df.drop(df[df['gender'].eq('male')].sample(n = (int((f_count*3)-m_count))))

#df = skew_dataset(df, 'gender', '25:75')
#print(df['gender'].value_counts(normalize = True))
#print(df)