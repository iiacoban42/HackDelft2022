import pandas as pd
import os

import warnings
warnings.filterwarnings('ignore')

data_folder = 'CGI-alles/Data/PMP Data/'

data = os.listdir(data_folder)

it = iter(data)
for datafile in it:
    next_dafatile = next(it)
    print (datafile, next_dafatile)

    name = datafile.split("_Motorstroomdata")[0]

    print(name)

    df_motor = pd.read_csv(data_folder + datafile, sep=";")

    df_motor = df_motor.drop("Assetnaam", 1)

    # print(df_motor)
    df_other = pd.read_csv(data_folder + next_dafatile, sep=";")

    df_other = df_other.drop("Assetnaam", 1)

    # print(df_other)

    combined = pd.concat([df_motor, df_other], ignore_index=True, sort=False)

    # print(combined)

    combined['Value'] = combined['Value'].apply(lambda x: x.replace(',','.') if isinstance(x, str) else x)

    # print(combined['Value'])

    combined.to_csv(f"src/combined_data/{name}_data.csv", encoding='utf-8', index=False)


print("done")