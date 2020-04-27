"""
This script contains different functions which transform a
column in a DataFrame which contains strings
"""
import pandas as pd

def split_string(filepath, split_char, split_num, col_name, new_col_name):
    """
    Parameters
    -----------
    filepath: str
        path to file to create dataframe

    split_char: str
        character which you want to split the string on

    split_num: int
        number which describes what value of the split you
        want to return

    col_name: str
        name of column which contains string where you want
        to apply split

    new_col_name: str
        name of the new column you want to store result
        of the split column
    """

    data_df = pd.read_csv(filepath)
    get_split = lambda string: string.split(split_char)[split_num]
    files_df[new_col_name] = files_df[col_name].apply(get_split)
    return data_df
