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
