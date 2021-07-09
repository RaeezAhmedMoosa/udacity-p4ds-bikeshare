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




# Practice Problem 1: Compute the Most Popular Start Hour
#
# Use pandas to load chicago.csv into a dataframe, and find the most frequent
# hour when people start traveling. There isn't an hour column in this dataset,
# but you can create one by extracting the hour from the "Start Time" column.
# To do this, you can convert "Start Time" to the datetime datatype using the
# pandas to_datetime() method and extracting properties such as the hour with
# these properties.
#
# Hint: Another way to describe the most common value in a column is the mode.
ch_df = pd.read_csv("../bikeshare-data/chicago.csv")

# Confirming that ch_df is a DataFrame object
type(ch_df)

# Checking the column names
ch_df.columns

# Viewing 5 rows of the "Start Time" column
ch_df["Start Time"].head()

# Verifying that "Start Time" is an object data type
ch_df.info()

# Viewing the first row of the "Start Time" column
ch_df["Start Time"][0]

# Obtaining the length of the characters in the first row of the "Start Time" column
len(ch_df["Start Time"][0])

# Extracting a slice of the value in the first row of the "Start Time" column
ch_df["Start Time"][0][11:13]

# This converts "Start Time" into the datetime64 data type
ch_df["Start Time"] = pd.to_datetime(ch_df["Start Time"])

# This creates a new column "Hour" by extracting the hour values from the "Start
#  Time" column
ch_df["Hour"] = ch_df["Start Time"].dt.hour

# This returns the modal value for the "Hours" column
popular_hour = ch_df["Hour"].mode()[0]




# Practice Problem 2: Display a Breakdown of User Types
#
# There are different types of users specified in the "User Type" column. Find
# how many there are of each type and store the counts in a pandas Series in the
# user_types variable.
#
# Hint: What pandas function returns a Series with the counts of each unique
# value in a column?
filename = "../bikeshare-data/chicago.csv"

df = pd.read_csv(filename)

type(df)

# Note that the .value_counts() method returns a pandas Series object when it
# (the method) is called on a DataFrame.
users_count = df["User Type"].value_counts()

# This confirms that "users_count" is a pandas Series object
type(users_count)

# These integer locations return the relevant Indices  in the pandas Series
users_count.iloc[0]
users_count.iloc[:]




# Practice Problem 3: Load and Filter the Dataset
#
# This is a bit of a bigger task, which involves choosing a dataset to load and
# filtering it based on a specified month and day. In the quiz below, you'll
# implement the load_data() function, which you can use directly in your project.
#
# There are four steps:
#
# 1. Load the dataset for the specified city. Index the global CITY_DATA dictionary
#    object to get the corresponding filename for the given city name.

# Step 1
cities_data = {
              "chicago" : "../bikeshare-data/chicago.csv",
              "new york city" : "../bikeshare-data/new_york_city.csv",
              "washington" : "../bikeshare-data/washington.csv"
}

# For Loop printing the Key Value pairs for the dictionary. Note the use of the
# items() method to achieve this.
for key, value in cities_data.items():
    print(key, value)

# For Loop printing the Keys from the dictionary. Note that when the dictionary
# is used like this in a For Loop, with no method being called on it, the default
# will be to return/print the Keys
for key in cities_data:
    print(key.title())

# For Loop printint the dictionary Values. Note the use of the values() method
# to achieve this
for value in cities_data.values():
    print(value)

#
def load_data(city):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(cities_data[city.lower()])
    print("This is the DataFrame for:", city.title())
    print(df.info())
    print(df.head())
    


load_data("NEW YORK CITY")
