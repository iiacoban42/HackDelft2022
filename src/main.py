import pandas as pd
import numpy as np
import os

# pd.set_option('display.float_format',  '{:,.5f}'.format)

frame = []
data_folder = os.getcwd() + '/CGI-alles/Data/PMP Data/'

df = pd.DataFrame(frame)

for datafile in os.listdir(data_folder):
    if os.path.isfile(datafile):
        df = pd.read_csv(datafile)
        index = df.index
        number_of_rows = len(index)
