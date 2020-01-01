import matplotlib.pyplot as plt
import pandas as pd
import os
csv_file = "crossword-clues-frequency-from-2019-01-01-to-2019-12-31.csv"
directory = "data"

my_path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(my_path, directory)
csv_path = os.path.join(data_path, csv_file)
print(csv_path)

# Read CSV file, get author names and counts.
df = pd.read_csv(csv_path, header=None,  usecols=[0,1], names=['answer', 'frequency'], nrows=10)

ax = df.plot.bar(x='answer', y='frequency', rot=0)
ax.plot()
plt.show()
