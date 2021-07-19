# This file will be used for the first build/version of the bikeshare program.
# The existing code imported from test_program can be refactored and new functions
# may be incorporated for the next build/version of bikeshare


# Imported Libraries, Modules and Packages
import datetime as dt
import time as tm
# sys is used for the type_print() function
import sys
import numpy as np
import pandas as pd


# Iterables

# Lists to be used within the obtain_month() and obtain_day() functions
months = ["none","january", "february", "march", "april", "may", "june"]

days = ["none", "monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday"]

# Dictionaries

# cities_data is the Dictionary which contains the files (and their directories)
# which will be used by the load_data() function. More cities can easily be added
# through the creation of a Key based on a specific city and then inserting the
# directory of the appropriate csv file
cities_data = {
              "chicago" : "../bikeshare-data/chicago.csv",
              "new york city" : "../bikeshare-data/new_york_city.csv",
              "washington" : "../bikeshare-data/washington.csv"
}

# stats_info is the Dictionary which will be used by the stats_calculator(),
# dictionary looper functions and the birth_stats() function to calculate the
# various Descriptive Statistics throughout the program
stats_info = {
              "mode times" : ["Hour", "Day of Week", "Month"],
              "mode trips" : ["Start Station", "End Station", "Trip"],
              "metrics trips" : ["Total Travel Time", "Average Travel Time",
                                 "Standard Deviation", "Median Travel Time"],
              "user info" : ["User Type Count", "Gender Count"],
              "birth info" : ["Earliest Birth Year", "Latest Birth Year", "Birth Year"]
}



# Formatting Functions

# type_print() function:
def type_print(text):
    '''
    This type_print function is an idea that I had which I think came from the
    Fallout game series, with the computer terminals in the game generating
    characters on the screen character-by-character. I thought it would look
    cool for certain sections to have this type writer sort of output so I wrote
    this function.

    I got the idea from a google search using the phrase "python print statement
    one character at a time". The following link had an answer to my query:

    Quora https://www.quora.com/How-do-I-print-one-character-at-a-time-in-the-terminal-using-Python
    (accessed 15 July 2021)

    INPUT:
    text: Any string, but please note that you cannot use the ',' character to
          join any variable to a print statement. Instead replace the ',' with
          the concatenation operator '+'

    OUTPUT:
    text: Same string as the INPUT but with each character in the string being
          printed one at a time.
    '''
    for ch in text:
        print(ch, end='')
        sys.stdout.flush()
        tm.sleep(0.05)

# print_pause() function:
#
# Simple function that will allow the information being displayed during the
# program to be returned to the user at a specified second interval. This will
# prevent a flood/avalanche of information being displayed to the user.
#
# The default parameter is 3 seconds, but this can be changed by passing a number
# to the function to have a shorter/longer pause depending on the circumstances
def print_pause(time=3):
    tm.sleep(time)

# line_break() function
#
# Basic function to implement line breaks within the text where necessary. The
# default number of line breaks is 1, but this can be changed by passing an
# integer to the function
def line_break(number=1):
    print("\n" * number)


# Calculation Time function

# time_calc()
#
# This function is the result of the refactoring of the sections of the code
# dealing with calculations, specifically the time it takes to perform these
# calculations. This function takes 2 parameters,being the Start time and the
# End time. It returns the time spent performing an action, in an interval which
# can be rounded according to the developer's discretion
def time_calc(start, end):
    print("Calculation time (seconds):", round((end - start), 3) )
    line_break()




# BikeShare functions

# Input related functions:

# Refactored obtain_input() function, which has been split across 3 functions.
# These functions all operate in the same way, with the only difference is the
# type of input that is obtained from the user.
#
# Note that, through testing, the variables within each of these 3 functions had
# to be made into global variables so that it could be returned to the function
# obtain_input() which called on these functions in the first place.
def obtain_city():
    global city
    type_print("\nWhich City would you like to view the BikeShare data for?\n")
    type_print("\nThe following Cities are in the database:\n")
    # To assist the user, the function will print out the names of the cities
    # that appear (as Keys) in the cities_data Dictionary. In this way, the user
    # can see the cities (and their spelling) before moving on to the input prompts.
    # Note that for this For Loop, the cities_data Dictionary has method called
    # on it, as the default in this case is to use the Dictionary Keys
    line_break()
    print_pause(1)
    for key in cities_data:
        print(key.title(), "\n")
    print_pause()
    # Note that for all the 3 input variables, the values will be converted to
    # lowercase by the lower() method, so that the values sync with the Dictionary
    # and List Keys and Elements
    city = input("\nPlease type in a city (use the full name):\n").lower()
    while city not in cities_data.keys():
        # A While Loop is implemented here (and for month and day) to handle any
        # invalid input entered by the user. Basically, if the entered input does not
        # exist in the respective Iterable, then the loop will run again until the
        # input is found in the Iterable.
        type_print("\nInvalid Input, please try again.\n")
        city = input("\nPlease type in a city (use the full name):\n").lower()
    return city

def obtain_month():
    global month
    type_print("\nWhich month would you like to use to view the Bikeshare data?\n")
    type_print("\nPlease type 'none' if you don't want to filter by month\n")
    type_print("\nThe database covers the following months:\n")
    print_pause(1)
    line_break()
    # To avoid confusion, the first element of the months List 'none' is excluded
    # when the code below is displayed to the user
    print(months[1:])
    print_pause()
    month = input("\nPlease type in a month (use the full name):\n").lower()
    while month not in months:
        type_print("\nInvalid Input, please try again.\n")
        month = input("\nPlease type in a month (use the full name):\n").lower()
    return month

def obtain_day():
    global day
    type_print("\nWhich day would you like to use to view the Bikeshare data?\n")
    type_print("\nPlease type 'none' if you don't want to filter by day\n")
    type_print("\nThe database covers the following days:\n")
    print_pause(1)
    line_break()
    # To avoid confusion, the first element of the days List 'none' is excluded
    # when the code below is displayed to the user
    print(days[1:])
    print_pause()
    day = input("\nPlease type in a day (use the full name):\n").lower()
    while day not in days:
        type_print("\nInvalid Input, please try again.\n")
        day = input("\nPlease type in a day (use the full name):\n").lower()
    return day

def obtain_input():
    obtain_city()
    obtain_month()
    obtain_day()
    type_print("\nInput - City: {}, Month: {}, Day: {}\n".format(city, month, day))
    load_data(city, month, day)


# Loading and Filtering functions:

# load_data()
def load_data(city, month="none", day="none"):
    '''
    This load_data() function receives all the input data from the obtain_input()
    function, and creates/loads the correspoding DataFrame. In doing so, this
    function also creates additional columns within the DataFrame that are not
    found in the original csv data. Additionall, this function also converts one
    of the columns 'Start Time' into a datetime data type/object.

    INPUT:
    city - string. csv file for a city as found in the cities_data dictionary.
    month - string. Month to be used to filter the data (optional).
    day - string. Day to be used to filter the data (optional)

    OUTPUT:
    DataFrame (df) - to be sent onwards for filtering
    '''
    df = pd.read_csv(cities_data[city])
    type_print("\nDataFrame created for: " + city.title())
    line_break(2)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    # This creates a new column with the months listed in the format month.title()
    df["Month"] = df["Start Time"].dt.strftime("%B")
    # This creates a new column with the days listed in the format day.title()
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    # This creates a new column "Trip" which is derived from the concatenation
    # of the "Start Station" and "End Station" columns. The string " to " is
    # added to make it clearer as to which Stations are which.
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    data_filter(city, df, month, day)

# data_filter()
def data_filter(city, df, month="none", day="none"):
    '''
    This data_filter() function takes the DataFrame from and any given filters
    from load_data(). If filters have been chosen, data_filter() uses Boolean
    Indexing to modify the DataFrame according to the filter(s).

    INPUT:
    city - string. To be passed on to the number_cruncher() function
    df - DataFrame. Created by load_data()
    month - string. Month to be used to filter the data (optional).
    day - string. Day to be used to filter the data (optional).
    '''
    if month != "none" and day == "none":
        print("\nFiltering by month:", month.title())
        df = df[df["Month"] == month.title()]
        line_break(3)
        number_cruncher(city, df)
    elif day != "none" and month == "none":
        print("\nFiltering by day:", day.title())
        df = df[df["Day of Week"] == day.title()]
        line_break(3)
        number_cruncher(city, df)
    elif month != "none" and day != "none":
        print("\nFiltering by day and month:", day.title(), month.title())
        # This is a Boolean Index which contains 2 conditions/filters. Through
        # testing, I found that I had issues when using the 'and' keyword to
        # connect the 2 conditions. It appears that the 2 conditions need to be
        # enclosed in brackets (which I had done) and that the '&' keyword must
        # be used to connect the conditions
        df = df[(df["Day of Week"] == day.title()) & (df["Month"] == month.title())]
        line_break(3)
        number_cruncher(city, df)
    elif month == "none" and day == "none":
        print("\nNo Filters are being applied.")
        line_break(3)
        number_cruncher(city, df)



# Statistical functions:

# Dictionary Looper functions

# Functions focused on the Modal (Most Popular) data
def dict_mode_looper(df, key, value):
    '''
    This is the dict_mode_looper() function. This function (and the other Dictionary
    looping functions) were created as a result of refactoring the code in the
    original stats_calculator(), counter() and birth_stats() functions. These
    functions streamlined the original 3 functions considerably in terms of the
    lines of code. This docstring applies to all the Dictionary looper functions.

    INPUT:
    df - DataFrame. Will be passed by the 3 original stats functions.
    key - string. Used to access the correct Key-Value pair.
    value - string. Actual value found in the Lists contained inside the Dictionary.

    OUTPUT:
    statistics - strings, integers and floats. Displayed to the user.
    '''
    # 1st Key in the stat_info Dictionary
    if key == "mode times":
        for n in range(len(stats_info[key])):
            start_time = tm.time()
            data = df[value[n]].mode()[0]
            # This extracts the count of the modal data obtained above, in
            # order to include it with the statistic printed by the function
            # Note that I experienced a KeyError when using the Washington
            # DataFrame where the code below was as follows:
            #
            # df[value[n]].value_counts()[0]
            #
            # I have added the integer location to be used as the Numerical
            # Index to avoid getting the KeyError. Curiously, this is not an
            # issue when working the with Chicago and NYC DataFrames
            count = df[value[n]].value_counts().iloc[0]
            end_time = tm.time()
            print_pause(4)
            print("Calculating statistic - Modal", value[n])
            print("\nMost Popular {}: {}".format(value[n], data))
            print("Count: {}".format(count))
            time_calc(start_time, end_time)
    # 2nd Key in the stat_info Dictionary
    elif key == "mode trips":
        for n in range(len(stats_info[key])):
            start_time = tm.time()
            data = df[value[n]].mode()[0]
            count = df[value[n]].value_counts().iloc[0]
            end_time = tm.time()
            print_pause(4)
            print("Calculating statistic - Modal", value[n])
            print("\nMost Popular {}: {}".format(value[n], data))
            print("Count: {}".format(count))
            time_calc(start_time, end_time)

def dict_metrics_looper(df, key, value):
    # 3rd Key in the stat_info Dictionary
    if key == "metrics trips":
        for n in range(len(stats_info[key])):
            # 0 == "Total Travel Time"
            if n == 0:
                start_time = tm.time()
                data = df["Trip Duration"].sum()
                end_time = tm.time()
                # To make the data a bit easier to understand for the user, the data
                # is refined further, by dividing it by 3600 (1 hour = 60 minutes * 60 seconds)
                # and then rounding off the quotient to avoid a long decimal trail.
                # This returns the Total Sum of "Trip Duration" in hours
                data_ref = round(data / 3600, 2)
                print_pause(4)
                print("Calculating statistic -", value[n])
                print("\n" + value[n], data_ref, "Hours")
                # Again, to refine the data even further to make it easier for the
                # user to understand, 'data_ref' is divided by 24 (1 day = 24 hours)
                # to return a rounded amount of Days for "Trip Duration" Total Sum
                data_days = round(data_ref / 24, 2)
                print(value[n], data_days, "Days")
                time_calc(start_time, end_time)
            # 1 == "Average Travel Time"
            elif n == 1:
                start_time = tm.time()
                data = df["Trip Duration"].mean()
                # Again, to make the data easier to understand for the user, the data
                # is refined by dividing it by 60 (1 minute = 60 seconds)
                data_ref = round(data / 60, 2)
                end_time = tm.time()
                print_pause(4)
                print("Calculating statistic -", value[n])
                print("\n" + value[n], data_ref, "Minutes")
                time_calc(start_time, end_time)
            # 2 == "Standard Deviation"
            elif n == 2:
                start_time = tm.time()
                data = df["Trip Duration"].std()
                data_ref = round(data /60, 2)
                end_time = tm.time()
                print_pause(4)
                print("Calculating statistic -", value[n])
                print("\n" + value[n], data_ref, "Minutes")
                time_calc(start_time, end_time)
            # 3 == "Median Travel Time"
            elif n == 3:
                start_time = tm.time()
                data = df["Trip Duration"].median()
                # Again, to make the data easier to understand for the user, the data
                # is refined by dividing it by 60 (1 minute = 60 seconds)
                data_ref = round(data / 60, 2)
                end_time = tm.time()
                print_pause(4)
                print("Calculating statistic -", value[n])
                print("\n" + value[n], data_ref, "Minutes")
                time_calc(start_time, end_time)

def dict_userinfo_looper(city, df, key, value):
    # Note that for this Dictionary Looper, the city is passsed as a Parameter
    # as Washington doesn't contain any 'Gender' data. Thus, to avoid a KeyError
    # being raised if the user selects Washington, the selected city must be
    # passed to this function as a safeguard.
    #
    # 4th Key in the stat_info Dictionary
    if key == "user info":
        for n in range(len(stats_info[key])):
            # 0 == "User Type Count"
            if n == 0:
                start_time = tm.time()
                # While testing this code block, I received a warning called
                # 'SettingwithCopyWarning'. This was not an error or exception
                # but a warning that a value is trying to be set on a copy
                # of a slice from a DataFrame.
                #
                # This was affecting the count for both "user info" elements
                # as the NaN replacement value was not being counted.
                #
                # To resolve this, I inserted the line below to create a
                # copy of the DataFrame before replacing the NaNs. This
                # has resolved the issue.
                df = df.copy()
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
                end_time = tm.time()
                print_pause(4)
                print(value[n], data)
                time_calc(start_time, end_time)
            # 0 == "Gender Count"
            elif n == 1 and city != "washington":
                start_time = tm.time()
                df = df.copy()
                df["Gender"].fillna("Not Specified", inplace=True)
                # This code follows the same logic and process as the count made for
                # "User Type"
                data = df.groupby(["Gender"])["Gender"].count()
                end_time = tm.time()
                print_pause(4)
                print(value[n], data)
                time_calc(start_time, end_time)

def dict_birthstats_looper(city, df, key, value):
    # Note that for this Dictionary Looper, the city is passsed as a Parameter
    # as Washington doesn't contain any 'Birth Year' data. Thus, to avoid a
    # KeyError being raised if the user selects Washington, the selected city
    # must be passed to this function as a safeguard
    #
    # 5th Key in the stat_info Dictionary
    if key == "birth info":
        for n in range(len(stats_info[key])):
            if n == 0 and city != "washington":
                start_time = tm.time()
                data = df["Birth Year"].min()
                # I see no reason for "Birth Year" to be a float type, so this
                # line converts "Birth Year" into an integer type
                data_int = int(data)
                end_time = tm.time()
                print_pause(4)
                print("{}: {}".format(value[n], data_int))
                # To make the data a bit more relatable, I have included this
                # line to indicate the possible age of the user with the
                # minimum age. The same has been done for the maximum and
                # modal age later on in the code
                print("Possible age in 2017:", 2017 - data_int)
                time_calc(start_time, end_time)
            elif n == 1 and city != "washington":
                start_time = tm.time()
                data = df["Birth Year"].max()
                data_int = int(data)
                end_time = tm.time()
                print_pause(4)
                print("{}: {}".format(value[n], data_int))
                print("Possible age in 2017:", 2017 - data_int)
                time_calc(start_time, end_time)
            elif n == 2 and city != "washington":
                start_time = tm.time()
                data = df[value[n]].mode()[0]
                data_int = int(data)
                count = df[value[n]].value_counts().iloc[0]
                end_time = tm.time()
                print_pause(4)
                print("Most Popular {}: {}".format(value[n], data_int))
                print("Count: {}".format(count))
                print("Possible age in 2017:", 2017 - data_int)
                time_calc(start_time, end_time)

# Descriptive Statistics functions:
def stats_calculator(df):
    for key, value in stats_info.items():
        dict_mode_looper(df, key, value)
        dict_metrics_looper(df, key, value)

def counter(city, df):
    for key, value in stats_info.items():
        dict_userinfo_looper(city, df, key, value)

def birth_stats(city, df):
    for key, value in stats_info.items():
        dict_birthstats_looper(city, df, key, value)


# User-related functions:

# data_viewer() - displays the DataFrame data to the user upon request
def data_viewer(df):
    print_pause(2)
    # These 2 variables are the slicing integers to be used to return 5 rows of
    # the raw data from the DataFrame each time the user inputs 'yes'
    x = 0
    y = 5
    print_pause(2)
    type_print("\nWould you like to see the raw BikeShare data?\n")
    choice = input("\nPlease type 'yes' to view the raw data.\n"
                   "Please type 'no' if you're not interested in the raw data."
                   "\n").lower()
    while choice not in ["yes", "no"]:
        type_print("\nInvalid Input, please try again.\n")
        choice = input("\nPlease type 'yes' to view the raw data.\n"
                       "Please type 'no' if you're not interested in the raw data."
                       "\n").lower()
    while choice == 'yes':
        print_pause(1)
        type_print("\nRaw data from the DataFrame incoming...\n")
        line_break()
        print_pause()
        # To remove ambiguity, the Numerical Indexing method is used
        print(df.iloc[x:y])
        choice = input("\nType 'yes' for more data.\n"
                       "Type 'no' to exit.\n").lower()
        # Each time the user responds with 'yes', the slice variables will
        # increase in value by 5, as to comply with the project specification of
        # displaying 5 rows of data at a time
        x += 5
        y += 5
        # In testing, I found that in this part of the program, the user could
        # input any text (except for 'yes') and the Loop would break. This was
        # a bug that I addressed by adding the code below
        if choice == 'no':
            # If the user inputs 'no' specifically, the Loop breaks
            break
        # This code block handles any invalid input entered by the user
        elif choice not in ["yes", "no"]:
            type_print("\nInvalid Input, please try again.\n")
            choice = input("\nType 'yes' for more data.\n"
                           "Type 'no' to exit.\n").lower()
    if choice == 'no':
        type_print("Thank you, we hope this experience has been informative.")
        line_break(3)

# conclusion() allows the user to either restart or quit the program
def conclusion():
    print_pause(2)
    choice = input("\nType 'restart' to restart.\n"
                   "Type 'quit' to exit the program.\n").lower()
    while choice not in ["restart", "quit"]:
        type_print("\nInvalid Input, please try again.\n")
        choice = input("\nType 'restart' to restart.\n"
                       "Type 'quit' to exit the program.\n").lower()
    if choice == "restart":
        type_print("Proceeding to restart the program...")
        line_break(20)
        obtain_input()
    elif choice == "quit":
        type_print("Thank you for using this program. Goodbye!")


# Structural/Wrapper functions:

# number_cruncher() - basically the heart\engine of the bikeshare program.
#
# To make it easier and simpler for the data to be crunched by the different
# functions, I have created this number_cruncher() function to send the
# returned data from data_filter() onwards
def number_cruncher(city, df):
    stats_calculator(df)
    counter(city, df)
    birth_stats(city, df)
    data_viewer(df)

# bikeshare() is a wrapper function which will be used in the final stages
# of the program
def bikeshare():
    obtain_input()
    conclusion()

# Test section

bikeshare()
