import pandas as pd


def get_summary_stats(df):
    """
    Return descriptive statistics for numeric columns in a DataFrame.
    """
    return df.describe()


def get_grouped_summary(df, group_col, numeric_col):
    """
    Return grouped summary statistics for a numeric column.
    """
    return (
        df.groupby(group_col)[numeric_col]
        .agg(["count", "mean", "median", "min", "max"])
        .reset_index()
    )

