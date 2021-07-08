# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import numpy as np
import pandas as pd

# Practice Problem 1
ch_df = pd.read_csv("../bikeshare-data/chicago.csv")

#print(ch_df.info())

ch_df["Start Time"] = pd.to_datetime(ch_df["Start Time"])

#print(ch_df.info())

#print(ch_df["Start Time"].head())

ch_df["Hour"] = ch_df["Start Time"].dt.hour

#print(ch_df["Hour"].head())

print(ch_df.head())

popular_hour = ch_df["Hour"].mode()[0]

print(popular_hour)
