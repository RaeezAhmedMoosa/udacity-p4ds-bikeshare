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


# 2. Create "month" and "day_of_week" columns. Convert the "Start Time" column to
#    datetime and extract the month number and weekday name into separate columns
#    using the datetime module.
#
# Step 2
def load_data(city):
    df = pd.read_csv(cities_data[city.lower()])
    df.info()
    # This converts the "Start Time" column object into a datetime64 object
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df.info()
    # This creates a "Month" column by extracting the month from "Start Time"
    df["Month"] = df["Start Time"].dt.month
    # This creates a "Day of Week" column by extracting the day from "Start Time"
    df["Day of Week"] = df["Start Time"].dt.day_name(locale = "English")
    df.info()


# 3. Filter by month. Since the month parameter is given as the name of the month,
#    you'll need to first convert this to the corresponding month number. Then,
#    select rows of the dataframe that have the specified month and reassign this
#    as the new dataframe.
#
# Step 3

# List consisting of the first 6 months of the year. I have included a "proxy"
# value as the first entry to make it easier to match the index of the month
# to their actual number in the sequence of months
months = ["proxy","january", "february", "march", "april", "may", "june"]

# This short if statement checks to see if a specific month is found in the
# List, and if it is, it prints the month's List Index integer value
if "january" in months:
    print(months.index("january"))


def load_data(city, month):
    df = pd.read_csv(cities_data[city.lower()])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["Day of Week"] = df["Start Time"].dt.day_name(locale = "English")
    # This is a List of the months covered by all the datasets
    months = ["proxy","january", "february", "march", "april", "may", "june"]
    # This takes the user inputted month and converts it into a lower case string
    month = month.lower()
    # This IF statement checks to see if the given month is in the List
    if month in months:
        # This converts the given month into an integer
        month = months.index(month)
        # This confirms that the month-integer conversion has occurred
        print(month)
        # This uses Boolean Indexing to create a new DataFrame which is filtered
        # based on the user provided month
        df = df[df["Month"] == month]
    return df.head()

# Another version of the working code:
def load_data(city, month):
    df = pd.read_csv(cities_data[city.lower()])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["Day of Week"] = df["Start Time"].dt.day_name(locale = "English")
    month = month.lower()
    if month != "all":
        months = ["proxy", "january", "february", "march", "april", "may", "june"]
        month = months.index(month)
        df = df[df["Month"] == month]
    return df.info(), df.head()

# 4. Filter by day of week. Select rows of the dataframe that have the specified
#    day of week and reassign this as the new dataframe. (Note: Capitalize the
#    day parameter with the title() method to match the title case used in the
#    day_of_week column!)
#
# Step 4


def load_data(city, month, day):
    df = pd.read_csv(cities_data[city.lower()])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["Day of Week"] = df["Start Time"].dt.day_name(locale = "English")
    months = ["proxy", "january", "february", "march", "april", "may", "june"]
    month = month.lower()
    if month in months:
        month = months.index(month)
        df = df[df["Month"] == month]
    # This is the IF statement  that will handle the "day" parameter
    if day != "all":
        # This Boolean Index creates a new DataFrame which is filtered based on
        # the selected day of the week.
        # This converts the given day into the proper format so that it will
        # match the format found within the DataFrame
        df = df[df["Day of Week"] == day.title()]
    return df.info(), df.head()

# Another working version of the code:
def load_data(city, month, day):
    df = pd.read_csv(cities_data[city.lower()])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    months = ["proxy", "january", "february", "march", "april", "may", "june"]
    month = month.lower()
    if month in months:
        month = months.index(month)
        df = df[df["Month"] == month]
    # This is the IF statement  that will handle the "day" parameter
    if day != "all":
        # This converts the given day into the proper format so that it will
        # match the format found within the DataFrame
        day = day.title()
        # This Boolean Index creates a new DataFrame which is filtered based on
        # the selected day of the week
        df = df[df["Day of Week"] == day]
    return df.info(), df.head()



# I want to convert the "Birth Year" column from a float into an integer
#
# So I first had to implement a way in which the code can identify that is working
# with a dataset that contains a "Birth Year" column (Chicago & NYC). I have done
# this using an IF statement with an IN expression.
#
#
def load_data(city):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    # This checks if the given city is either Chicago or New York
    if city.lower() in ["chicago", "new york city"]:
        # This replaces all the NaN values with the integer 0
        df.fillna(0, inplace=True)
        # This converts the "Birth Year" column dtype into an integer, but to do
        # so, all NaN values had to be substituted first
        df["Birth Year"] = df["Birth Year"].apply(np.int64)
    return df.isnull().any(), df.info(), df.head()




# Descriptive Statistics
#
# 1 - Popular Times of Travel
#
# I need to calculate the Mode for the following:
#
# 1. Month
# 2. Day of the Week
# 3. Hour

# This List contains the Modal elements that must be calculated for this part 1
# of the Descriptive Statistics
mode_times = ["Hour", "Day of Week", "Month"]

for stat in range(len(mode_times)):
    print("Calculating Statistic", stat)
    print("\nMost popular {}: ".format(mode_times[stat]))


def load_data(city):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    if city.lower() in ["chicago", "new york city"]:
        df.fillna(0, inplace=True)
        df["Birth Year"] = df["Birth Year"].apply(np.int64)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # This creates an "Hour" column derived from the hour value in "Start Time"
    df["Hour"] = df["Start Time"].dt.hour
    # To assist with the Descriptive Statistics later in the project, I have
    # converted the Month integer into its corresponding Month Name value by
    # using the dt.strftime("%B") method
    df["Month"] = df["Start Time"].dt.strftime("%B")
    # This creates an "Day of Week" column, also derived from "Start Time". To
    # make the data more informative for the user, the Days are returned in the
    # format of Day Name and not their integer equivalent
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    # This sends the created DataFrame to the stats_calculator() function so that
    # the statistics can be calculated and returned to the user
    return stats_calculator(df)


def stats_calculator(df):
    # This statement is to test whether or not the return made in load_data() is
    # successful, with load_data() returning a DataFrame at the end of the code
    print("Return Successful")
    # For this Modal set of stats (Most Popular Travel Times), this For Loop
    # cycles through the Modal stats for Hour, Day and Month and uses List Indexing
    # and DataFrame Manipulation to return the Mode for each item in the list.
    # To get the For Loop working correctly, the length of the List is wrapped
    # inside the range function, in this way, the For Loop will cycle through
    # the List according to the number of elements contained in the List.
    for stat in range(len(mode_times)):
        # This is where the DataFrame is manipulated to access the specific column
        # and then the mode() method is called to return the first (and only)
        # element in the array that is generated by the mode method.
        data = df[mode_times[stat]].mode()[0]
        print("Calculating Statistic: Modal", mode_times[stat])
        print("\nMost popular {}: {}".format(mode_times[stat], data))
    # For testing purposes, the DataFrame information and a sample of the DataFrame
    # is returned
    return df.info(), df.head()


# Descriptive Statistics
#
# 2 - Popular Stations & Trips
#
# I need to calculate the Mode for the following:
#
# 1. Start Station
# 2. End Station
# 3. Trip (most frequent Start Station + End Station Combination)

# This List contains the Modal elements that must be calculated for this part 2
# of the Descriptive Statistics
mode_trips = ["Start Station", "End Station", "Trip"]

def load_data(city):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    if city.lower() in ["chicago", "new york city"]:
        df.fillna(0, inplace=True)
        df["Birth Year"] = df["Birth Year"].apply(np.int64)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    # This creates a new column "Trip" which is derived from the concatenation
    # of the "Start Station" and "End Station" columns. The string " to " is
    # added to make it clearer as to which Stations are which.
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    return stats_calculator(df)

def stats_calculator(df):
    print("Return Successful!")
    for stat in range(len(mode_trips)):
        data = df[mode_trips[stat]].mode()[0]
        print("Calculating Statistic Modal:", mode_trips[stat])
        print("Most Popular {}: {}\n".format(mode_trips[stat], data))


# Descriptive Statistics
#
# 3 - Trip Duration
#
# I need to calculate the statistics for the following:
#
# 1. Total Travel Time
# 2. Average Travel Time
# 3. Median Travel Time

# This is a List containing elements with the names of the metrics that will be
# calculated for this part of Descriptive Statistics. Note that these names are
# NOT found within any of the DataFrames, so they should NOT be used when
# manipulating DataFrames
metrics_trip = ["Total Travel Time", "Average Travel Time", "Median Travel Time"]


def load_data(city):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    if city.lower() in ["chicago", "new york city"]:
        df.fillna(0, inplace=True)
        df["Birth Year"] = df["Birth Year"].apply(np.int64)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    return stats_calculator(df)

# This is test code. Basically I used a For Loop to cycle through the metrics_trip
# List, and depending on the integer value of 'stat', the Loop would print a
# specific element from the List. Again, because the names of the elements within
# the List are not found within the DataFrames, I can't use the For Loop method
# that I used when calculating the Modal values.
def stats_calculator(df):
    print("Return Successful!")
    print(df.info())
    for stat in range(len(metrics_trip)):
        if stat == 0:
            print(metrics_trip[stat])
        elif stat == 1:
            print(metrics_trip[stat])
        elif stat == 2:
            print(metrics_trip[stat])

def stats_calculator(df):
    print("Return Successful!")
    print(df.info())
    for stat in range(len(metrics_trip)):
        if stat == 0:
            # This calculates the Total Sum of "Trip Duration" in seconds
            data = df["Trip Duration"].sum()
            # To make the data a bit easier to understand for the user, the data
            # is refined further, by dividing it by 3600 (1 hour = 60 minutes * 60 seconds)
            # and then rounding off the quotient to avoid a long decimal trail.
            # This returns the Total Sum of "Trip Duration" in hours
            data_ref = round(data / 3600, 2)
            print("Calculating Statistics:", metrics_trip[stat])
            print(metrics_trip[stat], data_ref, "Hours\n")
            # Again, to refine the data even further to make it easier for the
            # user to understand, 'data_ref' is divided by 24 (1 day = 24 hours)
            # to return a rounded amount of Days for "Trip Duration" Total Sum
            data_days = round(data_ref / 24, 2)
            print(metrics_trip[stat], data_days, "Days\n")
        elif stat == 1:
            # This calculates the Average "Trip Duration" in seconds
            data = df["Trip Duration"].mean()
            # Again, to make the data easier to understand for the user, the data
            # is refined by dividing it by 60 (1 minute = 60 seconds)
            data_ref = round(data / 60, 2)
            print("Calculating Statistics:", metrics_trip[stat])
            print(metrics_trip[stat], data_ref, "Minutes\n")
        elif stat == 2:
            # This calculates the Median "Trip Duration" in seconds
            data = df["Trip Duration"].median()
            # Again, to make the data easier to understand for the user, the data
            # is refined by dividing it by 60 (1 minute = 60 seconds)
            data_ref = round(data / 60, 2)
            print("Calculating Statistics:", metrics_trip[stat])
            print(metrics_trip[stat], data_ref, "Minutes\n")


# Descriptive Statistics
#
# 4 - User Information
#
# I need to calculate the statistics for the following:
#
# 1. Counts of each User Type
# 2. Counts of each Gender
# 3. Earliest, Latest and Modal Birth Year

def load_data(city):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    # Lines 552 - 554 must be removed as this code is causing errors to occurr
    # in the "Birth Year" stats calculation
    if city.lower() in ["chicago", "new york city"]:
        df["Birth Year"].fillna(0, inplace=True)
        df["Birth Year"] = df["Birth Year"].apply(np.int64)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    return stats_calculator(df), counter(df)

def stats_calculator(df):
    # This code is added to verify the returns made by load_data()
    print("stats_calculator: Return Successful!")
    print(df.info())

# For the Count calculations, I am using a List containing the elements that
# will be Counted up in connection with User Information
user_info = ["User Type Count", "Gender Count"]

# Test code, For Loop printing the Index number and element of the user_info List
for n in range(len(user_info)):
    print(n, user_info[n])


# To keep the code looking neater and organised, I am using a separate function
# counter() to calculate Count statistics
def counter(city, df):
    print("counter: Return Successful!")
    print(df.info())
    for n in range(len(user_info)):
        if n == 0:
            # In cases where there are NaNs, the user type will be set to "Unkwown"
            df["User Type"].fillna("Unknown", inplace=True)
            # Similar to SQL (specifically Postgres), to obtain a count of each
            # "User Type", the data must be first grouped by "User Type". Then
            # the selected data "User Type" will be counted, and it will return
            # a table containing the total count for each user type
            #
            # The SQL code would be something like:
            #
            # SELECT user_type,
            #        COUNT(user_type) AS user_count
            # FROM df
            # GROUP BY 1
            # ORDER BY 2 DESC;
            data = df.groupby(["User Type"])["User Type"].count()
            print(user_info[n], data)
            # To make the data easier to read, I have included a print statement
            # which basically acts as a linebreak. I will create a simple function
            # line_break() when refactoring the code to replicate this code
            print("\n")
        elif n == 1:
            # The provided data has NaNs for "Gender" values. In these case, the
            # NaNs will be replaced with the value "Not Specified"
            df["Gender"].fillna("Not Specified", inplace=True)
            # This code follows the same logic and process as the count made for
            # "User Type"
            data = df.groupby(["Gender"])["Gender"].count()
            print(user_info[n], data)
            print("\n")


def counter(city, df):
    print(city.lower())
    print("counter: Return Successful!")
    print(df.info())
    for n in range(len(user_info)):
        if n == 0:
            df["User Type"].fillna("Unknown", inplace=True)
            data = df.groupby(["User Type"])["User Type"].count()
            print(user_info[n], data)
            print("\n")
        # In testing the counter() function, when loading the "washington" DF,
        # a KeyError was raised. This is due to the fact that the "washington"
        # DF does not contain a "Gender" column. To prevent this error from
        # occurring, I have used an expanded Logical condition to ensure that
        # only Chicago and NYC will return "Gender" counts
        elif n == 1 and city.lower() != "washington":
            df["Gender"].fillna("Not Specified", inplace=True)
            data = df.groupby(["Gender"])["Gender"].count()
            print(user_info[n], data)
            print("\n")

# For the "Birth Year" statistics, I am using another List which contains elements
# which will be used when calculating the relevant statistics
birth_list = ["Earliest Birth Year", "Latest Birth Year", "Birth Year"]


# To have the code be structured neatly and in an organised manner, I will use
# birth_stats() to calculate the statistics relating to the "Birth Year" column.
# Note that Washington does NOT contain a "Birth Year" column, thus there is no
# "Birth Year" data for Washington. As a result, just as with counter(), there
# are expanded Logical Statements which will handle
def birth_stats(city, df):
    print(city)
    for stat in range(len(birth_list)):
        if stat == 0 and city.lower() != "washington":
            data = df["Birth Year"].min()
            print(birth_list[stat], int(data))
            print("Possible Age in 2017:", 2017 - int(data))
            print("\n")
        elif stat == 1 and city.lower() != "washington":
            data = df["Birth Year"].max()
            print(birth_list[stat], int(data))
            print("Possible Age in 2017:", 2017 - int(data))
            print("\n")
        elif stat == 2 and city.lower() != "washington":
            data = df["Birth Year"].mode()[0]
            print("Most Popular {}: {}".format(birth_list[stat], int(data)))
            print("Possible Age in 2017:", 2017 - int(data))
            print("\n")




# Filtering the DataFrame
#
# The user should be provided with the option of filtering the data according to
# month or day or both (month and day)
def load_data(city, month=None, day=None):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    # This sends the Loaded DataFrame to the data_filter() function for the
    # Filtering of the DataFrame according to month, day or both
    return data_filter(df, month, day)


# This is the data_filter() function. I have decided to keep the loading and the
# filtering of the data separate in terms of function. I think I learned in the
# 'Intro to Programming' Nanodegree course that a function should have just one
# ...well function or purpose. I feel that combining the Loading and Filtering
# of a DataFrame in the same function will make the code hard to read and it
# would also be more difficult to debug in case of errors
#
# data_filter() receives the Loaded DataFrame from the load_data() function, with
# the filter(s) that the user wants to apply to the DataFrame. Through the use
# of Logical Conditions, the filters are then applied to the DataFrame. This
# data_filter() takes 3 parameters, witht the last 2 having a default of 'None'
#
# In this version of data_filter(), the DataFrame is returned to the user, but
# this is only for testing purposes. In the next stage, the DataFrame will be
# sent to the stats_calculator() function so that the Descriptive Statistics
# can then be computed. Also, this same filtered DataFrame must be sent to the
# counter() function for the User Info metrics to be calculated.
def data_filter(df, month=None, day=None):
    # Test statement for the function
    print("data_filter return successful!")
    # If the user has chosen to filter the DataFrame by month and not day, this
    # code block will be run
    if month != None and day == None:
        # Test Print Statement
        print("Filtering by month:", month.title())
        # Boolean indexing to filter the data according to the chosen month
        df = df[df["Month"] == month.title()]
        # Test Return to confirm that the filtering was correctly performed
        return df[["Month", "Day of Week"]].head(), df.info()
    # If the user has chosen to filter the DataFrame by day and not month, this
    # code block will be run
    elif day != None and month == None:
        # Test Print Statement
        print("Filtering by day:", day.title())
        # Boolean indexing to filter the data according to the chosen day
        df = df[df["Day of Week"] == day.title()]
        # Test Return to confirm that the filtering was correctly performed
        return df[["Day of Week", "Month"]].head(), df.info()
    # If the user has chosen to filter the DataFrame by day AND month, this
    # code block will be run
    elif month != None and day != None:
        # Test Print Statement
        print("Filtering by day and month:", day.title(), month.title())
        # This is a Boolean Index which contains 2 conditions/filters. Through
        # testing, I found that I had issues when using the 'and' keyword to
        # connect the 2 conditions. It appears that the 2 conditions need to be
        # enclosed in brackets (which I had done) and that the '&' keyword must
        # be used to connect the conditions
        df = df[(df["Day of Week"] == day.title()) & (df["Month"] == month.title())]
        # Test Return to confirm that the filtering was correctly performed
        return df[["Day of Week", "Month"]].head(), df.info()



# Descriptive Statistics
#
# After the loaded DataFrame has been filtered, the program must then take the
# DataFrame and calculate the the different Descriptive Statistics based on that
# filtered DataFrame

# Existing Code:
def load_data(city, month=None, day=None):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    return data_filter(df, month, day)

def data_filter(df, month=None, day=None):
    print("data_filter return successful!")
    if month != None and day == None:
        print("Filtering by month:", month.title())
        df = df[df["Month"] == month.title()]
        return stats_calculator(df)
    elif day != None and month == None:
        print("Filtering by day:", day.title())
        df = df[df["Day of Week"] == day.title()]
        return stats_calculator(df)
    elif month != None and day != None:
        print("Filtering by day and month:", day.title(), month.title())
        df = df[(df["Day of Week"] == day.title()) & (df["Month"] == month.title())]
        return stats_calculator(df)

# To make it easier to store all the different Lists that will be used by the
# stats_calculator() and counter() functions, I have stored all the Lists in a
# Dictionary, with the original List's variable name as the Key for each List
stats_info = {
              "mode times" : ["Hour", "Day of Week", "Month"],
              "mode trips" : ["Start Station", "End Station", "Trip"],
              "metrics trips" : ["Total Travel Time", "Average Travel Time", "Median Travel Time"],
              "user info" : ["User Type Count", "Gender Count"],
              "birth info" : ["Earliest Birth Year", "Latest Birth Year", "Birth Year"]
}

# This is test code, consisting of a For Loop within a For Loop (For Loop Inception)
# to test out the use of the stats_info Dictionary. The 1st For Loop prints out
# the Key, while the Inner For Loop prints out all the values found in the List
# connected to that key
for key, value in stats_info.items():
    print("Key:", key)
    for n in range(len(stats_info[key])):
        print("Value:", n, value[n])

#
def stats_calculator(df):
    print("stats_calculator currently operating...")
    return df.info()
