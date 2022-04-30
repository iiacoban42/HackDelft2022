import pandas as pd
import numpy as np
import os
# import matplotlib.pyplot as plt


# def get_boxplot(figname, data, labels):

#     fig = plt.figure(figsize =(10, 7))
#     # Creating axes instance

#     # Creating plot
#     bp = plt.boxplot(data)

#     # show plot
#     plt.savefig(figname+".jpeg")
#     plt.show()



# pd.set_option('display.float_format',  '{:,.5f}'.format)

frame = []
data_folder = 'CGI-alles/Data/PMP Data/'

df = pd.DataFrame(frame)

for datafile in os.listdir(data_folder):
    print(datafile)
    df = pd.read_csv(data_folder + datafile, sep=";")
    attr = df["Attribuut"].unique()
    asset = df["Assetnaam"].unique()

    print(attr)
    print(asset)



    break

