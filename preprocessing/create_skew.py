import numpy as np
import pandas as pd
import csv
import google
import os
import pathlib
import tqdm
import codecs
import shutil


def return_row_by_values(df, col, values):
    """
    This functions rewrites the dataframe by only having the desired
    values in the target column.
    ----------
    Params:
    df (DataFrame): Input DataFrame
    col (str): Target column
    values (lst): A list of strings
    ----------
    Returns:
    df (DataFrame): Output dataframe that only
                    contains the target values in the target column
    """
    return df[df[col].isin(values)]


def skew_calc(df, col, skew, max_samples):
    """
    This function calculates the value to apply to the pd.sample
    This allows it to create the desired skew.
    If the skew is not available it will tell you.
    ---------
    Params:
    df(DataFrame): Input dataframe
    col(str): Target column
    skew(list): List of strings of desired skew, where each element is of the form 'X-Y' and X+Y=100.
    max_samples(int): Maximum number of samples to be returned.
    ---------
    Returns:
    df(DataFrame): A filtered dataframe that satisfies the desired skew and has maximum max_samples rows.
    print(str): If the skew is wrong then a print string.
    """
    ratio = skew.split('-')
    if len(ratio) != 2:
        print(f"Invalid skew parameter: {skew}")
        return
    try:
        male_ratio, female_ratio = map(int, ratio)
    except ValueError:
        print(f"Invalid skew parameter: {skew}")
        return
    if male_ratio + female_ratio != 100:
        print(f"Invalid skew parameter: {skew}")
        return
    male_count = int(max_samples * male_ratio / 100)
    female_count = max_samples - male_count
    male_sample = df[df[col].eq('male')].sample(n=male_count)
    female_sample = df[df[col].eq('female')].sample(n=female_count)
    result_df = pd.concat([male_sample, female_sample])

    return result_df


def skew_dataset(df, col, skew):
    """
    This function calls the skew calculator
    so that the target values can be dropped from the input df
    Thus creating the desired skew.
    ----------
    Params:
    df(DataFrame): Input dataframe
    col(str): Target column
    skew(str): Str of desired skew: can only be '50:50', '25:75' or '75:25'
                at this point in time.
    ----------
    Returns:
    df(DataFrame): Output DataFrame that has the desired skew.
    """
    df = skew_calc(df, col, skew, max_samples=1000)
    return df


def keep_string_from_column(df, col):
    """
    Changes the column string to only return the sample part.
    -------
    Params:
    df (DataFrame): Input DataFrame
    col(str): Target column

    Returns:
    df (DataFrame): DataFrame that just has the desired string in target column
    """
    df[col] = df[col].apply(lambda x: x.split("/")[-1])
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
    # df = pd.read_csv(path, encoding='utf-16', delimiter = '\t')
    df = pd.read_table(path)  # , delimiter = '\t')
    df = df[['path', 'gender']]
    df = return_row_by_values(df, 'gender', ['male', 'female'])
    df = skew_dataset(df, 'gender', skew)

    # Create a list
    lst = df['path'].to_list()
    return lst, df
