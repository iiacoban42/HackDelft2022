import os
from xmlrpc.client import DateTime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import re



def get_boxplot(exp, data, labels):

    fig = plt.figure(figsize =(10, 7))
    # Creating axes instance

    # Creating plot
    bp = plt.boxplot(data)

    # show plot
    plt.savefig(exp+".jpeg")
    plt.show()


def get_plot_data(plot_name, attribute, df):
    # pd.set_option('display.float_format',  '{:,.5f}'.format)

    attr = df[attribute].unique()

    data = []
    boxplot_df = pd.DataFrame([])

    # print(attr)

    for att in attr:
        # filter rows by attribute
        # print(att)

        new_df = df[df[attribute]==att]
        # get values
        new_data = new_df["Value"]
        data.append(new_data)
        boxplot_df[att] = new_data

        daaata = {
            attr[0]: data[0]
        }
        # boxplot_df[factor_config[0]] =
        # boxplot_df[factor_config[1]] = data[1]

        boxplot_df = pd.DataFrame(new_df["Value"])
        # print(data)
        print(boxplot_df)

        myFig = plt.figure()
        bp = boxplot_df.boxplot()
        att = att.replace("/", "")
        print(f"{plot_name}_{att}.jpg")
        myFig.savefig(f"{plot_name}_{att}.jpg", format="jpg")

def check_equal_dates(date_1: DateTime, date_2: DateTime):
    return date_1.date() == date_2.date()

if __name__ == '__main__':

    frame = []
    # os.chdir("../")
    data_folder = 'src/combined_data/'

    df = pd.DataFrame(frame)

    files = os.listdir(data_folder)

    regex = ".*[a-zA-Z].*"

    for  datafile in files[0:1]:

        df = pd.read_csv(data_folder + datafile)

        df['Value'] = df['Value'].apply(lambda x: x if not re.match(regex, str(x)) else "DELETE")

        indexNames = df[df['Value'] == 'DELETE'].index

        df.drop(indexNames, inplace=True)

        df = df.astype({'Value': 'float'})

        print(df)
        # print(df["Attribuut"].unique())
        get_plot_data(f"{datafile[:-4]}", "Attribuut", df)
        # get_plot_data("plt2", "Assetnaam", df)
