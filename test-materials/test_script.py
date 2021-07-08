# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import numpy as np
import pandas as pd

# Practice Problem 2
filename = "../bikeshare-data/chicago.csv"

df = pd.read_csv(filename)

print(type(df))

users_count = df["User Type"].value_counts()

print(users_count)

print(type(users_count))

print(users_count.iloc[:])
