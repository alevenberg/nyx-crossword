import argparse
from collections import Counter
from datetime import date
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

MAX_CLUES = 30
def main():
    # Command line argument parsing
    parser = argparse.ArgumentParser(description='A script that scrapes https://nyxcrossword.com/ for the crossword clues and answers in the specified date range')
    parser.add_argument('-s', "--start_date",
        help="The start date - format YYYY-MM-DD",
        required=True,
        type=datetime.date.fromisoformat)
    parser.add_argument('-e', "--end_date",
        help="The end date - format YYYY-MM-DD (inclusive)",
        required=True,
        type=datetime.date.fromisoformat)
    
    args = parser.parse_args()

    start_date = args.start_date.strftime("%Y-%m-%d")
    end_date = args.end_date.strftime("%Y-%m-%d")

    csv_frequency_file = "crossword-clues-frequency-from-" + start_date + "-to-" + end_date + ".csv"
    data_directory = "data"
    my_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(my_path, data_directory)
    csv_frequency_file_path = os.path.join(data_path, csv_frequency_file)

    df = pd.read_csv(csv_frequency_file_path, header=None,  usecols=[0,1], names=['Answer', 'Frequency'], nrows=MAX_CLUES)

    df.plot('Answer', 'Frequency', kind='bar')
    plt.title("Most frequent NYT crossword answers from " + start_date + " to " + end_date , fontsize=13)  

    # Save figure
    graph_directory = "graph"
    image_file = "most-frequent-nyt-crossword-answers-from-" + start_date + "-to-" + end_date + ".png"
    graph_path = os.path.join(my_path, graph_directory)
    image_file_path = os.path.join(graph_path, image_file)
    plt.savefig(image_file_path, bbox_inches="tight");  

main()

