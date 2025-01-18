import csv
import json
import pandas as pd

data = pd.read_csv("instagram.csv")
print(data)
print("converted json file below..")
print(json.dumps(list(csv.reader(open("instagram.csv")))))
