# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import datetime as dt
import numpy as np
import pandas as pd

# Practice Problem 3
cities_data = {
              "chicago" : "../bikeshare-data/chicago.csv",
              "new york city" : "../bikeshare-data/new_york_city.csv",
              "washington" : "../bikeshare-data/washington.csv"
}

stats_info = {
              "mode times" : ["Hour", "Day of Week", "Month"],
              "mode trips" : ["Start Station", "End Station", "Trip"],
              "metrics trips" : ["Total Travel Time", "Average Travel Time", "Median Travel Time"],
              "user info" : ["User Type Count", "Gender Count"],
              "birth info" : ["Earliest Birth Year", "Latest Birth Year", "Birth Year"]
}


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
    print("\ndata_filter currently operating...\n")
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

def stats_calculator(df):
    print("\nstats_calculator currently operating...\n")



for key, value in stats_info.items():
    if key == "mode times":
        print("Descriptive Stats for Modal Times.\n")
        for n in range(len(stats_info[key])):
            print(key, n, value[n])
    elif key == "mode trips":
        print("\nDescriptive Stats for Modal Trips.\n")
        for n in range(len(stats_info[key])):
            print(key, n, value[n])

#
#print(load_data("new york city", "june", None))
