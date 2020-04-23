"""
"""
import os
import pandas as pd

def get_extension(filepath_column, csv_path):
    """
    Parameters
    ------------
    filepath_column: str
        the name of the column in the csv file which contains the filepath

    csv_path: the path to the csv file which to perform the operation

    Returns
    -----------
    files_df: DataFrame
        A Dataframe with a new column named "Extension" which has the
        extension of the filepath from the filepath_column
    """
    files_df = pd.read_csv(csv_path)
    get_ext = lambda filepath: os.path.splitext(filepath)[1].lower().strip()
    files_df['Extension'] = files_df[filepath_column].apply(get_ext)
    return files_df

def get_filename(filepath_column, csv_path):
    """
    Parameters
    ------------
    filepath_column: str
        the name of the column in the csv file which contains the filepath

    csv_path: the path to the csv file which to perform the operation

    Returns
    -----------
    files_df: DataFrame
        A Dataframe with a new column named "File Name" which has the
        filename from the filepath_column (name after last "/")
    """
    files_df = pd.read_csv(csv_path)
    get_filename = lambda filepath: os.path.basename(filepath)
    files_df['File Name'] = files_df[filepath_column].apply(get_filename)
    return files_df

def dir_after_dash_num(filepath_column, csv_path, dash_num):
    """
    Parameters
    ------------
    filepath_column: str
        the name of the column in the csv file which contains the filepath

    csv_path: the path to the csv file which to perform the operation

    Returns
    -----------
    files_df: DataFrame
        A Dataframe with a new column named "File Name" which has the
        filename from the filepath_column (name after last "/")
    """
    files_df = pd.read_csv(filepath)
    get_directory = lambda filepath: filepath.split('/')[dash_num]
    files_df['Person Dir'] = files_df[filepath_column].apply(get_directory)
    return files_df


