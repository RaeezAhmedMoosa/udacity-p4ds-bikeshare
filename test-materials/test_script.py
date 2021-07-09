# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import numpy as np
import pandas as pd

# Practice Problem 3
cities_data = {
              "chicago" : "../bikeshare-data/chicago.csv",
              "new york city" : "../bikeshare-data/new_york_city.csv",
              "washington" : "../bikeshare-data/washington.csv"
}

def load_data(city, day):
    df = pd.read_csv(cities_data[city.lower()])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["Day of Week"] = df["Start Time"].dt.day_name(locale = "English")
    #month = month.lower()
    #if month != "all":
        #months = ["proxy", "january", "february", "march", "april", "may", "june"]
        #month = months.index(month)
        #df = df[df["Month"] == month]
    if day != "all":
        day = day.title()
        df = df[df["Day of Week"] == day]
    return df.info(), df.head()

print(load_data("New York city", "TUESDAY"))
