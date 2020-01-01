import argparse
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

LAST_YEAR = 2019
EARLIEST_YEAR = 2019 # The earliest year to webscrape currently

def check_year(year):
    """ Input validation for the year """
    int_value = int(year)
    if int_value <= EARLIEST_YEAR && int_value <= LAST_YEAR:
        raise argparse.ArgumentTypeError("%s must be between 2011 and %s" % value LAST_YEAR)
    return int_value


# csv_file = "crossword-clues-from-2019-01-01-to-2019-12-31.csv"
# directory = "data"
# my_path = os.path.abspath(os.path.dirname(__file__))
# data_path = os.path.join(my_path, directory)
# csv_path = os.path.join(data_path, csv_file)
# print(csv_path)
# # Read CSV file, get author names and counts.
# df = pd.read_csv(csv_path, header=None,  usecols=[2], names=['answer'])
# # counter = Counter(df['answer'])
# # answer_names = counter.keys()
# # answer_counts = counter.values()

# # # Plot histogram using matplotlib bar().
# # indexes = np.arange(len(answer_names))
# # width = 0.7
# # plt.bar(indexes, answer_counts, width)
# # plt.xticks(indexes + width * 0.5, answer_names)
# # plt.show()

# csv_out_file = "crossword-clues-frequency-from-2019-01-01-to-2019-12-31.csv"
# csv_out_file_path = os.path.join(data_path, csv_out_file)
# value_counts = df['answer'].value_counts(ascending=False)
# value_counts.to_csv(csv_out_file_path)

# # ax = value_counts.plot.bar(x='answer', y='val', rot=0)
# # df['answer'].value_counts()
# # data = pd.read_csv(csv_path) 
# # data.head()

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
    parser.add_argument('-l', "--log_file",
        help="Logging file - default is app.log",
        required=False,
        default="crossword.log",
        type=argparse.FileType('w'))
    args = parser.parse_args()

    # Parse logging file
    my_path = os.path.abspath(os.path.dirname(__file__))
    log_file = os.path.join(my_path, str(args.log_file.name))
    logging.basicConfig(level=logging.INFO, filename=log_file, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

main()