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
    return df.info(), df.head()

print(load_data("ChIcAgO"))
