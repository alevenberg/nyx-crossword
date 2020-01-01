from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

csv_file = "crossword-clues-from-2019-01-01-to-2019-12-31.csv"
directory = "data"
my_path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(my_path, directory)
csv_path = os.path.join(data_path, csv_file)
print(csv_path)
# Read CSV file, get author names and counts.
df = pd.read_csv(csv_path, header=None,  usecols=[2], names=['answer'])
# counter = Counter(df['answer'])
# answer_names = counter.keys()
# answer_counts = counter.values()

# # Plot histogram using matplotlib bar().
# indexes = np.arange(len(answer_names))
# width = 0.7
# plt.bar(indexes, answer_counts, width)
# plt.xticks(indexes + width * 0.5, answer_names)
# plt.show()

csv_out_file = "crossword-clues-frequency-from-2019-01-01-to-2019-12-31.csv"
csv_out_file_path = os.path.join(data_path, csv_out_file)
value_counts = df['answer'].value_counts(ascending=False)
value_counts.to_csv(csv_out_file_path)

# ax = value_counts.plot.bar(x='answer', y='val', rot=0)
# df['answer'].value_counts()
# data = pd.read_csv(csv_path) 
# data.head()
