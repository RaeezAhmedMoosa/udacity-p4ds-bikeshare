# This file will be used to refactor the existing code from test_code.py and to
# write new functions that might be needed as a result of the refactoring


# Imported Libraries and Packages:
import datetime as dt
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

# load_data()
def load_data(city, month="none", day="none"):
    df = pd.read_csv(cities_data[city])
    print("\nDataFrame created for:", city.title())
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

# Dictionary Key function for trips metric data found in stats_info:
def dict_metrics_looper(df, key, value):
    if key == "metrics trips":
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
