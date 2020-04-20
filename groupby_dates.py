"""
Makes a bar graph with the dates on the x-axis.
The same dates will be grouped together
"""
import matplotlib.pyplot as plt
import pandas as pd

def groupby_year(datetime_df, date_col, sum_col):
    """
    Parameters
    -----------
    datetime_df: DateFrame 
        dateframe with datetime column

    date_col: str
        name of datetime column

    sum_col: str
        name of column which will be summed on grouping the dates
    
    graph_path: str path where graph will be saved

    Returns
    --------
    None

    
    """
    datetime_df = datetime_df.groupby(datetime_df[date_col].dt.year)\
            [sum_col].sum()
    return datetime_df

def groupby_year_month(datetime_df, date_col, sum_col):
    """
    """

    datetime_df[date_col + 'month'] = datetime_df[date_col].dt.month
    datetime_df[date_col + 'year'] = datetime_df[date_col].dt.year
    datetime_df.sort_values(date_col)
    datetime_df = datetime_df.groupby([date_col + 'year', date_col + 'month'])\
                                      [sum_col].sum()

    return datetime_df

def groupby_year_quarter(datetime_df, date_col, sum_col):


    datetime_df[date_col + 'quarter'] = datetime_df[date_col].dt.quarter
    datetime_df[date_col + 'year'] = datetime_df[date_col].dt.year
    datetime_df.sort_values(date_col)
    datetime_df = datetime_df.groupby([date_col + 'year', date_col + 'quarter'])\
                                      [sum_col].sum()

    return datetime_df
