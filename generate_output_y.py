import pandas as pd
import csv

x = list()
with open('x_dataset.csv', newline='') as readfile:
    reader = csv.reader(readfile)
    for row in reader:
        x.append(float(row[0]))

y = list()
for num in x:
    y.append(3*num + 6)

df_new = pd.DataFrame(y)
df_new.to_csv('y_dataset.csv', index=False, header=False)

