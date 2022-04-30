import os
from xmlrpc.client import DateTime

import pandas as pd
from matplotlib import pyplot as plt


def check_equal_dates(date_1: DateTime, date_2: DateTime):
    return date_1.date() == date_2.date()


frame = []
os.chdir("../")
data_folder = 'CGI-alles/Data/PMP Data/'

df = pd.DataFrame(frame)

for datafile in os.listdir(data_folder):
    print(datafile)

    df = pd.read_csv(data_folder + datafile, sep=";")
    print(df)
    x = list(range(0, len(df)))
    tstamp = df['Timestamp'][0]
    # df[check_equal_dates(df.Timestamp, tstamp)]

    df.reset_index().plot(x="index", y='Value', kind='scatter')
    plt.figure(figsize=(20, 10))
    plt.title(df['Attribuut'][0])
    plt.xscale('log')
    # plt.yscale('log')
    # plt.xlabel("Time")
    # plt.ylabel("Value")
    # # plt.xlim(10e-6, max(Q1))
    # plt.grid(True)
    # plt.legend()
    plt.show()
    break
