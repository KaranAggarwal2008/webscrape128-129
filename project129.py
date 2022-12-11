import pandas as pd
import csv
dataset_1=[]
dataset_2=[]
with open("project128.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)
with open("project127.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)
radius_column_old=dataset_1[4]
df=pd.read_csv("project128.csv")
df = df.dropna()
radius_column_new=radius_column_old
mass_column_old=dataset_1[3]
mass_column_new=mass_column_old
bright_stars_data=dataset_2[1:]
header_2=dataset_2[0]
header_1=dataset_1[0]
dataset_1[4].append(radius_column_new)
dataset_1[3].append(mass_column_new)
with open("project128.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)
project_128_data=dataset_1[1:]
headers=header_1+header_2
total_data=project_128_data+bright_stars_data
with open("project129.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(total_data)