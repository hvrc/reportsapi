from .utils import *
import io
import pymysql
# import pandas as pd

# Creates a pandas dataframe by reading a csv or a database table. To read a csv
# input must be a full csv file path. To read from a table, input must be a list
# of details: host, user, password, database, port and table.
def getDataframe(input):
    return pd.read_csv(input, dtype=object, encoding="ISO 8859-1") if isinstance(input, str) else pd.read_sql_query("SELECT * FROM %s" % (str(input[5])), pymysql.connect(host=str(input[0]), user=str(input[1]), password=str(input[2]), database=str(input[3]), port=int(input[4])))

# Converts a pandas dataframe to a csv and creates it at the output path
def createCSV(df, path, sep=","):
    df.to_csv(path, sep=sep, encoding="utf-8")

# Converts a normalized dataframe to a dataframe displaying the frequency of each
# instance, categorized by the columns specified in cols, and returns it; if type
# is "frequency", otherwise, function returns a dataframe displaying only the columns
# specified in cols, indexed by the first column specified in cols
def getReport(df, cols, type="frequency"):
    # format dates here
    df = formatDates(df, cols[0], "%d-%m-%Y")
    return pd.DataFrame(df.groupby(cols)[df.columns[0]].count()) if len(cols) == 1 else df.groupby(cols)[df.columns[0]].count().unstack().fillna(0) if type == "frequency" else df[cols[1:]].set_index(df[cols[0]])

# Returns a 'buffer' from a pandas dataframe. The buffer data is used by 'csvreport'
# to generate a csv in the view
def getBuffer(df, sep=","):
    # use utils functions here
    # df = appendSum(df, "columns")
    buffer = io.StringIO()
    df.to_csv(buffer, sep=sep, encoding="utf-8")
    buffer.seek(0)
    return buffer

# Returns a dictionary of values required by the c3.js script
# Rotates xticks if length of values is too large
def getChartResponse(df, width, height):
    width, height = int(width), int(height)
    columns, xTicks = list(df), list(df.index)
    xTicksRotate = -45 if (width - 200) / len(xTicks) < len(str(max(xTicks))) * 5 else 0
    values = [list(df[x]) for x in df]
    json = {columns[i] if len(values) > 1 else "Graph": values[i] for i in range(len(columns))}

    return {
        "json": json,
        "xTicks": xTicks,
        "xTicksRotate": xTicksRotate,
        "width": width,
        "height": height
    }

# Returns a dictionary of values required by the Kendo Stock script
def getKendoResponse(df, width, height):
    width, height = int(width), int(height)
    columns, xTicks = list(df), list(df.index)
    values = [list(df[x]) for x in df]
    data = []
    [[data.append({"%s" % (columns[i]): values[i][j], "date": xTicks[j]}) for j in range(len(values[i]))] for i in range(len(values))]

    return {
        "data": data,
        "columns": columns,
        "width": width,
        "height": height
    }
