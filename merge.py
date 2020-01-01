from collections import Counter
import csv
from datetime import date
import datetime
import glob
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

MAX_CLUES = 30

def read_csv(filename):
    """ Takea a file name and returns a dictionary where the first column
    is the key and the second is the value """
    reader = csv.reader(open(filename, 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = v
    return d

def main():
    data_directory = "data"
    my_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(my_path, data_directory)

    frequencies = {}
    for filename in glob.glob(os.path.join(data_path, 'crossword-clues-frequency-from-*.csv')):
        frequencies.update(read_csv(filename))

    frequency_list = [[k,int(v)] for k, v in frequencies.items()]
    df = pd.DataFrame(frequency_list, columns=['Answer', 'Frequency'])
    df = df.sort_values(by=['Frequency'], ascending=False)
    df = df.head(MAX_CLUES)

    df.plot('Answer', 'Frequency', kind='bar')
    plt.title("Most frequent NYT crossword answers from 2011 to 2019" , fontsize=13)

    # Save figure
    graph_directory = "graph"
    image_file = "most-frequent-nyt-crossword-answers.png"
    graph_path = os.path.join(my_path, graph_directory)
    image_file_path = os.path.join(graph_path, image_file)
    plt.savefig(image_file_path, bbox_inches="tight");

main()
