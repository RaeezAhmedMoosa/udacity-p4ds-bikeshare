# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import datetime as dt
import numpy as np
import pandas as pd

# Practice Problem 3
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


def load_data(city, month=None, day=None):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    data_filter(city, df, month, day)


def data_filter(city, df, month=None, day=None):
    print("\ndata_filter currently operating...\n")
    if month != None and day == None:
        print("Filtering by month:", month.title())
        df = df[df["Month"] == month.title()]
        number_cruncher(city, df)
    elif day != None and month == None:
        print("Filtering by day:", day.title())
        df = df[df["Day of Week"] == day.title()]
        number_cruncher(city, df)
    elif month != None and day != None:
        print("Filtering by day and month:", day.title(), month.title())
        df = df[(df["Day of Week"] == day.title()) & (df["Month"] == month.title())]
        number_cruncher(city, df)
    elif month == None and day == None:
        print("No Filters are being applied")
        number_cruncher(city, df)


def stats_calculator(df):
    print("\nstats_calculator() currently operating...\n")
    print(df[["Day of Week", "Month"]].head())
    for key, value in stats_info.items():
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
                    print(value[n], data)
                    print("\n")
                elif n == 1 and city.lower() != "washington":
                    df = df.copy()
                    df["Gender"].fillna("Not Specified", inplace=True)
                    data = df.groupby(["Gender"])["Gender"].count()
                    print(value[n], data)
                    print("\n")


def birth_stats(city, df):
    print("\nbirth_stats() currently operating...\n")
    print("Handling the", city.title(), "DataFrame\n")
    for key, value in stats_info.items():
        if key == "birth info":
            for n in range(len(stats_info[key])):
                if n == 0 and city.lower() != "washington":
                    data = df["Birth Year"].min()
                    data_int = int(data)
                    print("{}: {}".format(value[n], data_int))
                    print("Possible Age in 2017:", 2017 - data_int)
                    print("\n")
                elif n == 1 and city.lower() != "washington":
                    data = df["Birth Year"].max()
                    data_int = int(data)
                    print("{}: {}".format(value[n], data_int))
                    print("Possible Age in 2017:", 2017 - data_int)
                    print("\n")
                elif n == 2 and city.lower() != "washington":
                    data = df[value[n]].mode()[0]
                    data_int = int(data)
                    count = df[value[n]].value_counts().iloc[0]
                    print("Most Popular {}: {}".format(value[n], data_int))
                    print("Count: {}".format(count))
                    print("Possible Age in 2017:", 2017 - data_int)
                    print("\n")


def number_cruncher(city, df):
    print("\nnumber_cruncher() currently operating...\n")
    print("number_cruncher() is operating on the DataFrame for:", city.title())
    stats_calculator(df)
    print("\nstats_calculator() operation complete.")
    counter(city, df)
    print("\ncounter() operation complete.")
    birth_stats(city, df)
    print("\nbirth_stats() operation complete.")


def obtain_input():
    print("\nWhich City would you like to view the BikeShare data for?\n")
    print("The following Cities are in the database:\n")
    for key in cities_data:
        print(key.title())
    city = input("\nPlease type in a city (use the full name):\n").lower()
    while city not in cities_data.keys():
        print("\nInvalid Input, please try again.\n")
        city = input("\nPlease type in a city (use the full name):\n").lower()
    print(city)
    print("\nInput so far City: {}".format(city))
    print("\nWhich month would you like to use to view the Bikeshare data?\n")
    print("Please type 'none' if you don't want to filter by month\n")
    print("The database covers the following months:\n")
    print(months[1:])
    month = input("\nPlease type in a month (use the full name):\n").lower()
    while month not in months:
        print("\nInvalid Input, please try again.\n")
        month = input("\nPlease type in a month (use the full name):\n").lower()
    print(month)
    print("\nInput so far City: {}, Month: {}".format(city, month))
    print("\nWhich day would you like to use to view the Bikeshare data?\n")
    print("Please type 'none' if you don't want to filter by day\n")
    print("The database covers the following days:\n")
    print(days[1:])
    day = input("\nPlease type in a day (use the full name):\n").lower()
    while day not in days:
        print("\nInvalid Input, please try again.\n")
        day = input("\nPlease type in a day (use the full name):\n").lower()
    print(day)
    print("\nInput so far City: {}, Month: {}, Day: {}".format(city, month, day))
    print("\nReady to send Input data to the load_data() function!")





#obtain_input()


print(load_data("new york city", None, "FRiDaY"))
