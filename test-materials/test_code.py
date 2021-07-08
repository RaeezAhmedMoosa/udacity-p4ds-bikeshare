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
wdc_data = "./washington.csv"

wdc_data1 = "../bikeshare-data/washington.csv"

wdc_df = pd.read_csv(wdc_data)

type(wdc_df)



# Understanding the Data

# Chicago
ch_data1 = "../bikeshare-data/chicago.csv"

ch_df = pd.read_csv(ch_data1)

ch_df.head()

# There's 8 columns for the Chicago dataset
ch_df.columns
len(ch_df.columns)

# For the Chicago data, there are NaNs in the Gender and Birth Year columns
ch_df.isnull().any()

# Returns Descriptive Statistics for the "Trip Duration" and "Birth Year" columns
ch_df.describe()

# This provides the data type and count (Non-Null values) for each column
# An issue I have picked up here is that the "Birth Year" column is of the float
# data type. I must look into converting this into an integer
ch_df.info()

# This returns a count of the different values contained within the "Gender"
# column. Originally, I used this on the "Start Time" column, but then I realised
# the method counts each value in the column
ch_df["Gender"].value_counts()

# This returns a count of the values, but the count is grouped by gender in terms
# of the count of "User Type"
ch_df[["Gender", "User Type"]].value_counts()

# This returns a list of all the unique Starting Stations in the Chicago dataset
ch_df["Start Station"].unique()

# This returns the number of unique Starting Stations in the Chicago dataset
len(ch_df["Start Station"].unique())
