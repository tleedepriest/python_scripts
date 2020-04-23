"""
This script groups the data by year and plots them as a histogram
"""
import pandas as pd

def transform_dates_column(file_path, date_column_name, string_time_format):
    """
    Parameters
    -------------
    file_path: str
        the file_path to the csv file

    date_column_name: str
        the name of the column to transform into datetime format

    string_time_format: str
        dates of date column string time format
        example: date 05/7/2017 ---> '%m/%d/%Y'
        
        see https://strftime.org/ for all stringtime formats

    Returns
    --------------
    df: DataFrame

        Old column which contained dates in old df 
        transformed into Datetime. Rows are dropped
        if date column doesn't contain same format
        as stringtime format.
    
    """
    df = pd.read_csv(file_path)
    print("Df shape before transforming date column: {}\n".format(df.shape))
    print("Df stats: {}\n".format(df.describe()))
    print(df.head())
    df[date_column_name] = pd.to_datetime(df[date_column_name],\
                                            format = string_time_format,\
                                            errors = 'coerce')
    df = df[df[date_column_name].notna()]
    print("Df shape after transforming date column: {}\n".format(df.shape))
    print("Df stats: {}\n".format(df.describe()))
    print(df.head())
    return df

