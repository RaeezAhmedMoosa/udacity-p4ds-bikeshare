# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import numpy as np
import pandas as pd

# File Directory Tests
ch_data1 = "../bikeshare-data/chicago.csv"

ch_df = pd.read_csv(ch_data1)

print(ch_df.head())

print(ch_df.columns)

print(ch_df.isnull().any())

print(ch_df.describe())

print(ch_df.info())

print(ch_df["Gender"].value_counts())

print(ch_df[["Gender", "User Type"]].value_counts())

print(ch_df["Start Station"].unique())

print(len(ch_df["Start Station"].unique()))
