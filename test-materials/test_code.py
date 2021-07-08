# This file will be used to write all the initial code for the "Bikeshare" project
# This file will not be included in the final version of the project code
import numpy as np
import os
import pandas as pd

# File Directory Tests
ch_data = "./chicago.csv"

ch_data1 = "../bikeshare-data/chicago.csv"

ch_df = pd.read_csv(ch_data)

os.getcwd()
