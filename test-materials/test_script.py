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


def load_data(city):
    df = pd.read_csv(cities_data[city.lower()])
    print("DataFrame created for:", city.title())
    if city.lower() in ["chicago", "new york city"]:
        df.fillna(0, inplace=True)
        df["Birth Year"] = df["Birth Year"].apply(np.int64)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # This creates an "Hour" column derived from the hour value in "Start Time"
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    return stats_calculator(df)

mode_times = ["Hour", "Day of Week", "Month"]


#def stats_calculator(df):
    #for n in range(len(mode_times)):
        #print(mode_times[n], n + 1)

def stats_calculator(df):
    print("Return Successful")
    for stat in range(len(mode_times)):
        data = df[mode_times[stat]].mode()[0]
        print("Calculating Statistic: Modal", mode_times[stat])
        print("Most popular {}: {}\n".format(mode_times[stat], data))
    return df.info(), df.head()



print(load_data("WAshington"))
