import csv
from matplotlib import pyplot as plt

x = list()
y = list()

with open('x_dataset.csv', newline='') as x_readfile:
    reader_x = csv.reader(x_readfile)
    for row_x in reader_x:
        x.append(float(row_x[0]))

with open('y_dataset.csv', newline='') as y_readfile:
    reader_y = csv.reader(y_readfile)
    for row_y in reader_y:
        y.append(float(row_y[0]))


plt.figure(figsize=(10, 8))
plt.scatter(x, y, c='b', label='data')
plt.title('Equation y = 3x+6', fontsize=20)
plt.xlabel("x", fontsize=20)
plt.ylabel("y", fontsize=20)
plt.savefig('equation_graph.png')