import pandas as pd
import random

random_nums = list()
for point in range(0,1000):
    random_nums.append(random.uniform(0,101))

df = pd.DataFrame(random_nums)
df.to_csv('x_dataset.csv', index=False, header=False)