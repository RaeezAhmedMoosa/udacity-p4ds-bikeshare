# This file will be used as a testing ground, from which code written in the
# "test_code" file will be run. This file will not be included in the final
# version of the "Bikeshare" project.
import datetime as dt
import time as tm
import sys
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


def type_print(text):
    for ch in text:
        print(ch, end='')
        sys.stdout.flush()
        tm.sleep(0.05)

def print_pause(time=3):
    tm.sleep(time)


def load_data(city, month="none", day="none"):
    df = pd.read_csv(cities_data[city])
    type_print("\nDataFrame created for: " + city.title())
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    df["Month"] = df["Start Time"].dt.strftime("%B")
    df["Day of Week"] = df["Start Time"].dt.strftime("%A")
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    data_filter(city, df, month, day)


def data_filter(city, df, month="none", day="none"):
    print("\ndata_filter() currently operating...\n")
    if month != "none" and day == "none":
        print("Filtering by month:", month.title())
        df = df[df["Month"] == month.title()]
        number_cruncher(city, df)
    elif day != "none" and month == "none":
        print("Filtering by day:", day.title())
        df = df[df["Day of Week"] == day.title()]
        number_cruncher(city, df)
    elif month != "none" and day != "none":
        print("Filtering by day and month:", day.title(), month.title())
        df = df[(df["Day of Week"] == day.title()) & (df["Month"] == month.title())]
        number_cruncher(city, df)
    elif month == "none" and day == "none":
        print("No Filters are being applied")
        number_cruncher(city, df)


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

def dict_userinfo_looper(city, df, key, value):
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

def dict_birthstats_looper(city, df, key, value):
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


def stats_calculator(df):
    print("\nstats_calculator() currently operating...\n")
    print(df[["Day of Week", "Month"]].head())
    for key, value in stats_info.items():
        dict_mode_looper(df, key, value)
        dict_metrics_looper(df, key, value)


def counter(city, df):
    print("\ncounter() currently operating...\n")
    print("Handling the", city.title(), "DataFrame\n")
    for key, value in stats_info.items():
        dict_userinfo_looper(city, df, key, value)


def birth_stats(city, df):
    print("\nbirth_stats() currently operating...\n")
    print("Handling the", city.title(), "DataFrame\n")
    for key, value in stats_info.items():
        dict_birthstats_looper(city, df, key, value)

def conclusion():
    print("\nconclusion() currently operating...\n")
    print_pause(2)
    choice = input("Type 'restart' to restart.\n"
                   "Type 'quit' to exit the program.\n").lower()
    while choice not in ["restart", "quit"]:
        type_print("\nInvalid Input, please try again.\n")
        choice = input("\nType 'restart' to restart.\n"
                       "Type 'quit' to exit the program.\n").lower()
    if choice == "restart":
        type_print("Proceeding to restart the program...")
        obtain_input()
    elif choice == "quit":
        type_print("Thank you for using this program. Goodbye!")


def number_cruncher(city, df):
    print("\nnumber_cruncher() currently operating...\n")
    print("number_cruncher() is operating on the DataFrame for:", city.title())
    stats_calculator(df)
    print("\nstats_calculator() operation complete.")
    counter(city, df)
    print("\ncounter() operation complete.")
    birth_stats(city, df)
    print("\nbirth_stats() operation complete.")
    data_viewer(df)
    print("\ndata_viewer() operation complete.")
    conclusion()



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


def obtain_input():
    obtain_city()
    obtain_month()
    obtain_day()
    type_print("\nInput so far City: {}, Month: {}, Day: {}\n".format(city, month, day))
    load_data(city, month, day)


def data_viewer(df):
    print("\ndata_viewer() currently operating...\n")
    print_pause(2)
    print(df[["Day of Week", "Month"]].head())
    x = 0
    y = 5
    print_pause(2)
    type_print("\nWould you like to see the raw BikeShare data?\n")
    choice = input("\nPlease type 'yes' to view the raw data.\n"
                   "Please type 'no' if you're not interested in the raw data."
                   "\n").lower()
    while choice not in ["yes", "no"]:
        type_print("\nInvalid Input, please try again.\n")
        choice = input("\nPlease type 'yes' to view the raw data.\n"
                       "Please type 'no' if you're not interested in the raw data."
                       "\n").lower()
    while choice == 'yes':
        print_pause(1)
        print("\nRaw data from the DataFrame incoming...\n")
        print_pause()
        print(df.iloc[x:y])
        choice = input("\nType 'yes' for more data.\n"
                       "Type 'no' to exit.\n").lower()
        x += 5
        y += 5
    if choice == 'no':
        type_print("Thank you, we hope this experience has been informative.")






obtain_input()


#print(load_data("new york city", None, "FRiDaY"))
