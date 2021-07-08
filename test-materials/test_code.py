# This file will be used to write all the initial code for the "Bikeshare" project
# This file will not be included in the final version of the project code
import numpy as np
import pandas as pd

# File Directory Tests

# Chicago
ch_data = "./chicago.csv"

ch_data1 = "../bikeshare-data/chicago.csv"

ch_df = pd.read_csv(ch_data)

type(ch_df)




# New York City
nyc_data = "./new_york_city.csv"

nyc_data1 = "../bikeshare-data/new_york_city.csv"

nyc_df = pd.read_csv(nyc_data1)

type(nyc_df)


# Washington
