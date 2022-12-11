import pandas as pd
import csv
df = pd.read_csv("project129.csv")
del df["Luminosity"]
del df["Radius"]
df.to_csv('main.csv') 