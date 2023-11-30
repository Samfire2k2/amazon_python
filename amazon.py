import csv
import pandas as pd

df = pd.read_csv('.\bestsellers with categories.csv')

print(df.to_string()) 