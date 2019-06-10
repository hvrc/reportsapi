from datetime import (datetime, timedelta, date)
import pandas as pd

# converts full names in the specified column to either the first or last name depending
# on the specified index
def formatNames(df, column, index, sep=" "):
    df[column] = df.apply(lambda x: x[column].split(sep)[index], axis=1)
    return df

# formats dates in the specified column into the specified format
def formatDates(df, column, format="%d-%m-%Y %H:%M:%S"):
    df[column] = pd.to_datetime(df[column]).dt.strftime(format)
    return df

# returns a list of unique values from the specified column
def getUnique(df, column, key=str):
    return sorted(list(set(df[column])), key=key) if key == "str" else sorted(list(set(df[column])), key=key)

# appends the sum of all the values in the row or column (specified by the axis)
# to the dataframe
def appendSum(df, axis, title="Total"):
    if axis in "columns": df[title] = df.sum(1)
    elif axis in "rows": df.loc[title] = [df[x].sum() for x in list(df)]
    return df

# appends the average of all the values in each of the rows or columns (specified
# by the axis) to the dataframe
def appendAverage(df, axis, title="Average"):
    if axis in "columns": df[title] = df.mean(1).round(2)
    elif axis in "rows": df.loc[title] = [df[x].mean().round(2) for x in list(df)]
    return df
