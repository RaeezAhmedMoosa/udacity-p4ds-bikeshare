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


def load_data(city):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    return stats_calculator(df), counter(city, df), birth_stats(city, df)


def stats_calculator(df):
    print("stats_calculator: Return Successful!")
    print(df.info())

user_info = ["User Type Count:", "Gender Count:"]

def counter(city, df):
    print(city)
    print("counter: Return Successful!")
    print(df.info())
    for n in range(len(user_info)):
        if n == 0:
            df["User Type"].fillna("Unknown", inplace=True)
            data = df.groupby(["User Type"])["User Type"].count()
            print(user_info[n], data)
            print("\n")
        elif n == 1 and city.lower() != "washington":
            df["Gender"].fillna("Not Specified", inplace=True)
            data = df.groupby(["Gender"])["Gender"].count()
            print(user_info[n], data)
            print("\n")

birth_list = ["Earliest Birth Year:", "Latest Birth Year:", "Birth Year"]

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

#
print(load_data("wAsHiNgToN"))
