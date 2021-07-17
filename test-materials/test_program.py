# This file will be used to refactor the existing code from test_code.py and to
# write new functions that might be needed as a result of the refactoring


# Imported Libraries and Packages:
import datetime as dt
import time as tm
import sys
import numpy as np
import pandas as pd


# Iterables
months = ["none","january", "february", "march", "april", "may", "june"]

days = ["none", "monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday"]


cities_data = {
              "chicago" : "../bikeshare-data/chicago.csv",
              "new york city" : "../bikeshare-data/new_york_city.csv",
              "washington" : "../bikeshare-data/washington.csv"
}

stats_info = {
              "mode times" : ["Hour", "Day of Week", "Month"],
              "mode trips" : ["Start Station", "End Station", "Trip"],
              "metrics trips" : ["Total Travel Time", "Average Travel Time",
                                 "Standard Deviation", "Median Travel Time"],
              "user info" : ["User Type Count", "Gender Count"],
              "birth info" : ["Earliest Birth Year", "Latest Birth Year", "Birth Year"]
}


# Functions section

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
    for ch in test:
        print(ch, end='')
        sys.stdout.flush()
        tm.sleep(0.05)


# print_pause() function:
#
# Simple function that will allow the information being displayed during the
# program to be returned to the user at a 3 second interval. This will prevent a
# flood/avalanche of information being displayed to the user.
#
# The default parameter is 3 seconds, but this can be changed by passing a number
# to the function to have a shorter/longer pause depending on the circumstances
def print_pause(time=3):
    tm.sleep(time)


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
    print("\n")
    print_pause(1)
    for key in cities_data:
        print(key.title(), "\n")
    print_pause()
    city = input("\nPlease type in a city (use the full name):\n").lower()
    while city not in cities_data.keys():
        type_print("\nInvalid Input, please try again.\n")
        city = input("\nPlease type in a city (use the full name):\n").lower()
    return city


def obtain_month():
    global month
    type_print("\nWhich month would you like to use to view the Bikeshare data?\n")
    type_print("\nPlease type 'none' if you don't want to filter by month\n")
    type_print("\nThe database covers the following months:\n")
    print_pause(1)
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
    print(days[1:])
    print_pause()
    day = input("\nPlease type in a day (use the full name):\n").lower()
    while day not in days:
        type_print("\nInvalid Input, please try again.\n")
        day = input("\nPlease type in a day (use the full name):\n").lower()
    return day



# load_data()
def load_data(city, month="none", day="none"):
    df = pd.read_csv(cities_data[city])
    type_print("\nDataFrame created for:" + city.title())
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    data_filter(city, df, month, day)


# data_filter()
def data_filter(city, df, month="none", day="none"):
    print("\ndata_filter() currently operating...\n")
    if month != "none" and day == "none":
        df = df[df["Month"] == month.title()]
        number_cruncher(city, df)
    elif day != "none" and month == "none":
        df = df[df["Day of Week"] == day.title()]
        number_cruncher(city, df)
    elif month != "none" and day != "none":
        df = df[(df["Day of Week"] == day.title()) & (df["Month"] == month.title())]
        number_cruncher(city, df)
    elif month == "none" and day == "none":
        number_cruncher(city, df)

# Dictionary Key function for the modal data found in stats_info:
def dict_mode_looper(df, key, value):
    if key == "mode times":
        for n in range(len(stats_info[key])):
            data = df[value[n]].mode()[0]
            count = df[value[n]].value_counts().iloc[0]
            print_pause(4)
            print("Calculating statistic Modal", value[n])
            print("\nMost Popular {}: {}".format(value[n], data))
            print("Count: {}\n".format(count))
    elif key == "mode trips":
        for n in range(len(stats_info[key])):
            data = df[value[n]].mode()[0]
            count = df[value[n]].value_counts().iloc[0]
            print_pause(4)
            print("Calculating statistic Modal", value[n])
            print("\nMost Popular {}: {}".format(value[n], data))
            print("Count: {}\n".format(count))

# Dictionary Key function for trips metric data found in stats_info:
def dict_metrics_looper(df, key, value):
    if key == "metrics trips":
        for n in range(len(stats_info[key])):
            if n == 0:
                data = df["Trip Duration"].sum()
                data_ref = round(data / 3600, 2)
                print_pause(4)
                print("Calculating Statistics", value[n])
                print("\n" + value[n], data_ref, "Hours")
                data_days = round(data_ref / 24, 2)
                print(value[n], data_days, "Days\n")
            elif n == 1:
                data = df["Trip Duration"].mean()
                data_ref = round(data / 60, 2)
                print_pause(4)
                print("Calculating Statistics", value[n])
                print("\n" + value[n], data_ref, "Minutes\n")
            elif n == 2:
                data = df["Trip Duration"].std()
                data_ref = round(data /60, 2)
                print_pause(4)
                print("Calculating Statistics", value[n])
                print("\n" + value[n], data_ref, "Minutes\n")
            elif n == 3:
                data = df["Trip Duration"].median()
                data_ref = round(data / 60, 2)
                print_pause(4)
                print("Calculating Statistics", value[n])
                print("\n" + value[n], data_ref, "Minutes\n")


# Dictionary Key function for the user info data found in stats_info:
def dict_userinfo_looper(city, df, key, value):
    # Note that for this Dictionary Looper, the city is passsed as a Parameter
    # as Washington doesn't contain any 'Gender' data. Thus, to avoid a KeyError
    # being raised if the user selects Washington, the selected city must be
    # passed to this function as a safeguard.
    if key == "user info":
        for n in range(len(stats_info[key])):
            if n == 0:
                df = df.copy()
                df["User Type"].fillna("Unknown", inplace=True)
                data = df.groupby(["User Type"])["User Type"].count()
                print_pause(4)
                print(value[n], data)
                print("\n")
            elif n == 1 and city.lower() != "washington":
                df = df.copy()
                df["Gender"].fillna("Not Specified", inplace=True)
                data = df.groupby(["Gender"])["Gender"].count()
                print_pause(4)
                print(value[n], data)
                print("\n")


# Dictionary Key function for the birth info data found in stats_info:
def dict_birthstats_looper(city, df, key, value):
    # Note that for this Dictionary Looper, the city is passsed as a Parameter
    # as Washington doesn't contain any 'Birth Year' data. Thus, to avoid a
    # KeyError being raised if the user selects Washington, the selected city
    # must be passed to this function as a safeguard.
    if key == "birth info":
        for n in range(len(stats_info[key])):
            if n == 0 and city.lower() != "washington":
                data = df["Birth Year"].min()
                data_int = int(data)
                print_pause(4)
                print("{}: {}".format(value[n], data_int))
                print("Possible Age in 2017:", 2017 - data_int)
                print("\n")
            elif n == 1 and city.lower() != "washington":
                data = df["Birth Year"].max()
                data_int = int(data)
                print_pause(4)
                print("{}: {}".format(value[n], data_int))
                print("Possible Age in 2017:", 2017 - data_int)
                print("\n")
            elif n == 2 and city.lower() != "washington":
                data = df[value[n]].mode()[0]
                data_int = int(data)
                count = df[value[n]].value_counts().iloc[0]
                print_pause(4)
                print("Most Popular {}: {}".format(value[n], data_int))
                print("Count: {}".format(count))
                print("Possible Age in 2017:", 2017 - data_int)
                print("\n")


# stats_calculator() test_code version
def stats_calculator(df):
    print("\nstats_calculator() currently operating...\n")
    print(df[["Day of Week", "Month"]].head())
    for key, value in stats_info.items():
        # I have decided to refactor the code dealing with the modal data found
        # in the stats_info Dictionary. The new function dict_mode_looper() will
        # now contain the code below which handles the Keys "mode times" and
        # "mode trips"
        if key == "mode times":
            for n in range(len(stats_info[key])):
                data = df[value[n]].mode()[0]
                count = df[value[n]].value_counts().iloc[0]
                print("Calculating statistic Modal", value[n])
                print("\nMost Popular {}: {}".format(value[n], data))
                print("Count: {}\n".format(count))
        elif key == "mode trips":
            for n in range(len(stats_info[key])):
                data = df[value[n]].mode()[0]
                count = df[value[n]].value_counts().iloc[0]
                print("Calculating statistic Modal", value[n])
                print("\nMost Popular {}: {}".format(value[n], data))
                print("Count: {}\n".format(count))
        # Just like with modal data, the metrics trips data code will be refactored
        # into a separate function dict_metrics_looper().
        elif key == "metrics trips":
            for n in range(len(stats_info[key])):
                if n == 0:
                    data = df["Trip Duration"].sum()
                    data_ref = round(data / 3600, 2)
                    print("Calculating Statistics", value[n])
                    print("\n" + value[n], data_ref, "Hours")
                    data_days = round(data_ref / 24, 2)
                    print(value[n], data_days, "Days\n")
                elif n == 1:
                    data = df["Trip Duration"].mean()
                    data_ref = round(data / 60, 2)
                    print("Calculating Statistics", value[n])
                    print("\n" + value[n], data_ref, "Minutes\n")
                elif n == 2:
                    data = df["Trip Duration"].std()
                    data_ref = round(data /60, 2)
                    print("Calculating Statistics", value[n])
                    print("\n" + value[n], data_ref, "Minutes\n")
                elif n == 3:
                    data = df["Trip Duration"].median()
                    data_ref = round(data / 60, 2)
                    print("Calculating Statistics", value[n])
                    print("\n" + value[n], data_ref, "Minutes\n")

# stats_calculator() test_progam version:
def stats_calculator(df):
    print("\nstats_calculator() currently operating...\n")
    print(df[["Day of Week", "Month"]].head())
    for key, value in stats_info.items():
        # Thanks to the refactoring of the code, this new function has been
        # reduced from 24 Lines to 6 Lines
        dict_mode_looper(df, key, value)
        dict_metrics_looper(df, key, value)


# obtain_input() test_code version:
def obtain_input():
    print("\nWhich City would you like to view the BikeShare data for?\n")
    print("The following Cities are in the database:\n")
    for key in cities_data:
        print(key.title())
    city = input("\nPlease type in a city (use the full name):\n").lower()
    while city not in cities_data.keys():
        print("\nInvalid Input, please try again.\n")
        city = input("\nPlease type in a city (use the full name):\n").lower()
    print("\nWhich month would you like to use to view the Bikeshare data?\n")
    print("Please type 'none' if you don't want to filter by month\n")
    print("The database covers the following months:\n")
    print(months[1:])
    month = input("\nPlease type in a month (use the full name):\n").lower()
    while month not in months:
        print("\nInvalid Input, please try again.\n")
        month = input("\nPlease type in a month (use the full name):\n").lower()
    print("\nWhich day would you like to use to view the Bikeshare data?\n")
    print("Please type 'none' if you don't want to filter by day\n")
    print("The database covers the following days:\n")
    print(days[1:])
    day = input("\nPlease type in a day (use the full name):\n").lower()
    while day not in days:
        print("\nInvalid Input, please try again.\n")
        day = input("\nPlease type in a day (use the full name):\n").lower()
    print("\nInput so far City: {}, Month: {}, Day: {}".format(city, month, day))
    load_data(city, month, day)

# obtain_input() test_program version 1:
def obtain_input():
    # The type_print() function will only be implemented for input related text
    # strings only, as testing type_print() with the other functions resulted in
    # numerous formatting issues and exceptions being raised
    type_print("\nWhich City would you like to view the BikeShare data for?\n")
    type_print("\nThe following Cities are in the database:\n")
    print("\n")
    print_pause(1)
    for key in cities_data:
        print(key.title(), "\n")
    print_pause()
    city = input("\nPlease type in a city (use the full name):\n").lower()
    while city not in cities_data.keys():
        type_print("\nInvalid Input, please try again.\n")
        city = input("\nPlease type in a city (use the full name):\n").lower()
    type_print("\nWhich month would you like to use to view the Bikeshare data?\n")
    type_print("\nPlease type 'none' if you don't want to filter by month\n")
    type_print("\nThe database covers the following months:\n")
    print_pause(1)
    # Attempting to use type_print() below results in a string being printed
    # with all the months in one line, with no spaces separating them. Thus avoid
    # using type_print for anything other than plain text.
    print(months[1:])
    print_pause()
    month = input("\nPlease type in a month (use the full name):\n").lower()
    while month not in months:
        type_print("\nInvalid Input, please try again.\n")
        month = input("\nPlease type in a month (use the full name):\n").lower()
    type_print("\nWhich day would you like to use to view the Bikeshare data?\n")
    type_print("\nPlease type 'none' if you don't want to filter by day\n")
    type_print("\nThe database covers the following days:\n")
    print_pause(1)
    print(days[1:])
    print_pause()
    day = input("\nPlease type in a day (use the full name):\n").lower()
    while day not in days:
        type_print("\nInvalid Input, please try again.\n")
        day = input("\nPlease type in a day (use the full name):\n").lower()
    type_print("\nInput so far City: {}, Month: {}, Day: {}\n".format(city, month, day))
    load_data(city, month, day)


# counter() test_code version:
def counter(city, df):
    print("\ncounter() currently operating...\n")
    print("Handling the", city.title(), "DataFrame\n")
    for key, value in stats_info.items():
        if key == "user info":
            for n in range(len(stats_info[key])):
                if n == 0:
                    df = df.copy()
                    df["User Type"].fillna("Unknown", inplace=True)
                    data = df.groupby(["User Type"])["User Type"].count()
                    print_pause(4)
                    print(value[n], data)
                    print("\n")
                elif n == 1 and city.lower() != "washington":
                    df = df.copy()
                    df["Gender"].fillna("Not Specified", inplace=True)
                    data = df.groupby(["Gender"])["Gender"].count()
                    print_pause(4)
                    print(value[n], data)
                    print("\n")

# counter() test_program version:
def counter(city, df):
    print("\ncounter() currently operating...\n")
    print("Handling the", city.title(), "DataFrame\n")
    for key, value in stats_info.items():
        # Thanks to the refactoring of the code, this new function has been
        # reduced from 20 Lines to 5 Lines
        dict_userinfo_looper(city, df, key, value)


# birth_stats() test_code version:
def birth_stats(city, df):
    print("\nbirth_stats() currently operating...\n")
    print("Handling the", city.title(), "DataFrame\n")
    for key, value in stats_info.items():
        if key == "birth info":
            for n in range(len(stats_info[key])):
                if n == 0 and city.lower() != "washington":
                    data = df["Birth Year"].min()
                    data_int = int(data)
                    print_pause(4)
                    print("{}: {}".format(value[n], data_int))
                    print("Possible Age in 2017:", 2017 - data_int)
                    print("\n")
                elif n == 1 and city.lower() != "washington":
                    data = df["Birth Year"].max()
                    data_int = int(data)
                    print_pause(4)
                    print("{}: {}".format(value[n], data_int))
                    print("Possible Age in 2017:", 2017 - data_int)
                    print("\n")
                elif n == 2 and city.lower() != "washington":
                    data = df[value[n]].mode()[0]
                    data_int = int(data)
                    count = df[value[n]].value_counts().iloc[0]
                    print_pause(4)
                    print("Most Popular {}: {}".format(value[n], data_int))
                    print("Count: {}".format(count))
                    print("Possible Age in 2017:", 2017 - data_int)
                    print("\n")

# birth_stats() test_program version:
def birth_stats(city, df):
    print("\nbirth_stats() currently operating...\n")
    print("Handling the", city.title(), "DataFrame\n")
    for key, value in stats_info.items():
        # Thanks to the refactoring of the code, this new function has been
        # reduced from 29 Lines to 5 Lines
        dict_birthstats_looper(city, df, key, value)


# obtain_input() test_program version 1:
def obtain_input():
    # The type_print() function will only be implemented for input related text
    # strings only, as testing type_print() with the other functions resulted in
    # numerous formatting issues and exceptions being raised
    type_print("\nWhich City would you like to view the BikeShare data for?\n")
    type_print("\nThe following Cities are in the database:\n")
    print("\n")
    print_pause(1)
    for key in cities_data:
        print(key.title(), "\n")
    print_pause()
    city = input("\nPlease type in a city (use the full name):\n").lower()
    while city not in cities_data.keys():
        type_print("\nInvalid Input, please try again.\n")
        city = input("\nPlease type in a city (use the full name):\n").lower()
    type_print("\nWhich month would you like to use to view the Bikeshare data?\n")
    type_print("\nPlease type 'none' if you don't want to filter by month\n")
    type_print("\nThe database covers the following months:\n")
    print_pause(1)
    # Attempting to use type_print() below results in a string being printed
    # with all the months in one line, with no spaces separating them. Thus avoid
    # using type_print for anything other than plain text.
    print(months[1:])
    print_pause()
    month = input("\nPlease type in a month (use the full name):\n").lower()
    while month not in months:
        type_print("\nInvalid Input, please try again.\n")
        month = input("\nPlease type in a month (use the full name):\n").lower()
    type_print("\nWhich day would you like to use to view the Bikeshare data?\n")
    type_print("\nPlease type 'none' if you don't want to filter by day\n")
    type_print("\nThe database covers the following days:\n")
    print_pause(1)
    print(days[1:])
    print_pause()
    day = input("\nPlease type in a day (use the full name):\n").lower()
    while day not in days:
        type_print("\nInvalid Input, please try again.\n")
        day = input("\nPlease type in a day (use the full name):\n").lower()
    type_print("\nInput so far City: {}, Month: {}, Day: {}\n".format(city, month, day))
    load_data(city, month, day)


# obtain_input() test_program version 2:
def obtain_input():
    # Thanks to the refactoring of the code, this new function has been
    # reduced from 34 Lines to 6 Lines
    obtain_city()
    obtain_month()
    obtain_day()
    type_print("\nInput entered - City: {} Month: {} Day: {}\n".format(city, month, day))
    load_data(city, month, day)


# Now I need to create a function that will allow the user to view the raw data
# of the DataFrame that the program created and used to calculate all the various
# statistics found in the program.
#
# This function should also give the user the option to view 5 rows of data at a
# time, with an option to keep viewing 5 more rows. The user must also be given
# the choice to leave the viewing of the raw data and/or to not view the data
# at all when first prompted to do so.
#
# This function should operate after the number_cruncher() function, after all
# the Descriptive Statistics have been calculated

# data_viwer() version 1:
def data_viewer(df):
    # TPS to verify that the data_viewer() function is operating within the program
    print("\ndata_viewer() currently operating...\n")
    print_pause(2)
    # TPS to verify that, in the event of a filtered DataFrame, the actual filtered
    # DataFrame is being used
    print(df[["Day of Week", "Month"]].head())
    # These 2 variables are the slicing integers to be used to return 5 rows of
    # the raw data from the DataFrame each time the user inputs 'yes'
    x = 0
    y = 5
    print_pause(2)
    type_print("\nWould you like to see the raw BikeShare data?\n")
    choice = input("\nPlease type 'yes' to view the raw data.\n"
                   "Please type 'no' if you're not interested in the raw data."
                   "\n").lower()
    # While Loop to validate the input and handle any invalid input
    while choice not in ["yes", "no"]:
        type_print("\nInvalid Input, please try again.\n")
        choice = input("\nPlease type 'yes' to view the raw data.\n"
                       "Please type 'no' if you're not interested in the raw data."
                       "\n").lower()
   # While Loop that handles the printing of the raw DataFrame data each time the
   # user wants to view the data.
    while choice == 'yes':
        print_pause(1)
        # Print statement to make the user aware that the program will be
        # displaying the requested data
        print("\nRaw data from the DataFrame incoming...\n")
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
    if choice == 'no':
        type_print("Thank you, we hope this experience has been informative.")
