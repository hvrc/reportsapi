import sys
sys.path.append("..")
from _source.reporter import *

df = getDataframe("Users/Harsh/Desktop/reportsapi/_examples/_files/visits.csv")
# names = getUnique(df, "full_name")
df = getReport(df, ["date_time", "full_name"], "frequency")
createCSV(df, "Users/Harsh/Desktop/reportsapi/_examples/_files/report.csv")
