import argparse
from bs4 import BeautifulSoup
import csv
from datetime import date
import datetime
import logging
import os
import pandas as pd
import requests
import sys 
import urllib.parse

def generate_dates(start_date, end_date):
    """Return a list of dates"""
    return pd.date_range(start=start_date, end=end_date)

def store_clue(clue_dict, item, logger):
    """Stores an item into a dictionary"""
    key = item[0]
    answer = item[1]
    logger.debug("Storing clue '{}' with answer '{}'".format(key, answer))
    clue_dict[key] = answer

def get_clues(url, logger):
    """Return a dictionary containing the clues and answers of the crossword from the given page"""
    logger.info("Scraping clues from '{}'".format(url))
    page = None
    try: 
        page = requests.get(url)
    except requests.exceptions.ConnectionError: 
        logger.error("Unable to connect to url '{}'".format(url))
        return {}

    if (page is None):
        logger.error("Unable to connect to url '{}'".format(url))
        return {}

    soup = BeautifulSoup(page.text, "lxml")
    clue_list_p = soup.find("div", {"id":"clue_list"})

    if (clue_list_p is None):
        logger.error("Unable to parse page - no clue list found '{}'".format(url))
        return {}

    clue_list = []
    for item in clue_list_p.find_all("p"):
        text = item.get_text()
        clue_list.extend(text.split("\n"))

    clue_list = list(filter(lambda x: x != "",clue_list)) # Remove empty string entry

    clues = {}
    for item in clue_list:
        logger.debug("Parsing clue '{}' from url '{}'".format(item, url))
        item = item.lstrip('0123456789') # Remove number from front
        item = item.lstrip() # Remove white space from front
        # Split clue and answer if separated with colon
        if (item.find(".") == 0):
            # For case, #. Clue [2019-02-06]
            # Edge case in [2019-01-02], #. Clue: Clue cont : Answer
            item = item.lstrip(". ") # Remove white space from front
            if (item.count(":") != 1):
                item = item.rpartition(":")
                clue = item[0]
                answer = item[2]
                item = [clue, answer]
            else:
                item = item.split(":")
            store_clue(clues, [x.strip() for x in item], logger)
        elif (":" in  item):
            # Edge case in [2019-07-11], # Clue:Answer
            if (item.count(":") != 1):
                item = item.rpartition(":")
                clue = item[0]
                answer = item[2]
                item = [clue, answer]
            else:
                item = item.split(":")
            store_clue(clues, [x.strip() for x in item], logger)
        elif (item.find("…") == 0):
            item = item.lstrip("…")
            if (item.find("..") != -1):
                item = item.split("..")
                store_clue(clues, item, logger)
            elif (item.find("…") != 0):
                item = item.split("…")
                store_clue(clues, item, logger)
        else: 
            if (item != "Down"):
                logger.error("Unable to parse item '{}' from '{}'".format(item, url))
    
    return clues

def write_to_csv(crossword_dict, date, file_name, logger):
    """Writes to a csv file for a given date"""
    logger.info("Writing to csv file '{}' for {}".format(file_name, date))

    # Make directory in file it is run in
    directory = "data"
    my_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(my_path, directory)

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    csv_path = os.path.join(data_path, file_name)

    mode = "w"
    if (os.path.exists(csv_path)):
        mode = "a"

    with open(csv_path, mode) as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            escapechar=' ', quoting=csv.QUOTE_MINIMAL)
        for clue, answer in crossword_dict.items():
            writer.writerow([date, clue, answer])

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
    logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # Validate dates
    start_date = args.start_date.strftime("%Y-%m-%d")
    end_date = args.end_date.strftime("%Y-%m-%d")

    if (end_date < start_date):
        logger.warning("End date must be after or the same as the start date")
        sys.exit(0)

    todays_date = date.today().strftime("%Y-%m-%d")
    if (end_date > todays_date):
        logger.warning("End date must be before today")
        sys.exit(0)

    # Generate dates
    date_range = generate_dates(args.start_date, args.end_date)

    base_url = "https://nyxcrossword.com"

    if (args.start_date != args.end_date):
        file_name = "crossword-clues-from-" + str(args.start_date) + "-to-" + str(args.end_date) + ".csv"
    else: 
        file_name = "crossword-clues-from-" + str(args.start_date) + ".csv"

    for single_date in date_range:
        year = single_date.strftime("%Y")
        month = single_date.strftime("%m")
        day = single_date.strftime("%d")
        url_date_items = [year, month, day]
        
        url = urllib.parse.urljoin(base_url, ("/".join(url_date_items)))

        clues_dict = get_clues(url, logger)
        
        # Write to csv
        write_to_csv(clues_dict, single_date.strftime("%Y-%m-%d"), file_name, logger)

main()