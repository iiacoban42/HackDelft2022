import pandas as pd
import os

import warnings
warnings.filterwarnings('ignore')

data_folder = 'CGI-alles/Data/PMP Data/'

data = os.listdir(data_folder)

switch_names = []

for filename in data:
    if filename.__contains__("_Motorstroomdata"):
        name = filename.split("_Motorstroomdata")[0]
        switch_names.append(name)

# print(switch_names)
# print(len(switch_names))

# it = iter(data)
# for datafile in it:
for name in switch_names:
    motor_file = f'{name}_Motorstroomdata.csv'
    other_file = f'{name}_otherdata.csv'
    print(motor_file)
    print(other_file)

    df_motor = pd.read_csv(data_folder + motor_file, sep=";")

    df_motor = df_motor.drop("Assetnaam", 1)

    # print(df_motor)
    df_other = pd.read_csv(data_folder + other_file, sep=";")

    df_other = df_other.drop("Assetnaam", 1)

    # print(df_other)

    combined = pd.concat([df_motor, df_other], ignore_index=True, sort=False)

    # print(combined)

    combined['Value'] = combined['Value'].apply(lambda x: x.replace(',','.') if isinstance(x, str) else x)

    # print(combined['Value'])

    combined.to_csv(f"src/combined_data/{name}_data.csv", encoding='utf-8', index=False)


print("done")