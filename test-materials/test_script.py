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
    if city.lower() in ["chicago", "new york city"]:
        df.fillna(0, inplace=True)
        df["Birth Year"] = df["Birth Year"].apply(np.int64)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    return stats_calculator(df)


metrics_trip = ["Total Travel Time", "Average Travel Time", "Median Travel Time"]

def stats_calculator(df):
    print("Return Successful!")
    print(df.info())
    for stat in range(len(metrics_trip)):
        if stat == 0:
            data = df["Trip Duration"].sum()
            data_ref = round(data / 3600, 2)
            print("Calculating Statistics:", metrics_trip[stat])
            print(metrics_trip[stat], data_ref, "Hours\n")
            data_days = round(data_ref / 24, 2)
            print(metrics_trip[stat], data_days, "Days\n")
        elif stat == 1:
            data = df["Trip Duration"].mean()
            data_ref = round(data / 60, 2)
            print("Calculating Statistics:", metrics_trip[stat])
            print(metrics_trip[stat], data_ref, "Minutes\n")
        elif stat == 2:
            data = df["Trip Duration"].median()
            data_ref = round(data / 60, 2)
            print("Calculating Statistics:", metrics_trip[stat])
            print(metrics_trip[stat], data_ref, "Minutes\n")


print(load_data("WASHington"))
