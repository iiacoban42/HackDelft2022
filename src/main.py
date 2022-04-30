import pandas as pd
import numpy as np
import os

frame = []
data_folder = 'CGI-alles/Data/PMP Data/'

df = pd.DataFrame(frame)

for datafile in os.listdir(data_folder):
    print(datafile)

    df = pd.read_csv(data_folder + datafile)
    print(df)
