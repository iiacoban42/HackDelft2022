import os
from xmlrpc.client import DateTime

import pandas as pd
from matplotlib import pyplot as plt



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

    for att in attr:
        # filter rows by attribute
        new_df = df[df[attribute]==att]
        # get values
        new_data = new_df["Value"]
        data.append(new_data)
        boxplot_df[att] = new_data

    daaata = {
        attr[0]: data[0],
        attr[1]: data[1]

    }
    # boxplot_df[factor_config[0]] =
    # boxplot_df[factor_config[1]] = data[1]

    boxplot_df = pd.DataFrame(daaata)
    print(data)
    print(boxplot_df)

    myFig = plt.figure()
    bp = boxplot_df.boxplot()
    myFig.savefig(plot_name+".jpg", format="jpg")

def check_equal_dates(date_1: DateTime, date_2: DateTime):
    return date_1.date() == date_2.date()


frame = []
# os.chdir("../")
data_folder = 'CGI-alles/Data/PMP Data/'

df = pd.DataFrame(frame)

for datafile in os.listdir(data_folder):
    print(datafile)
    df = pd.read_csv(data_folder + datafile, sep=";")
    get_plot_data("plt1", "Attribuut", df)
    get_plot_data("plt2", "Assetnaam", df)

    break
