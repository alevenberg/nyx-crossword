from bs4 import BeautifulSoup
import requests
import re
import csv
import os
import os.path
import csv 
import argparse
import datetime
import pandas as pd
import urllib.parse
import sys 

def generate_dates(start_date, end_date):
    """Return a list of dates"""
    return pd.date_range(start=start_date, end=end_date)

def store_clue(clue_dict, item):
    """Stores an item into a dictionary"""
    key = item[0]
    answer = item[1]
    clue_dict[key] = answer

def get_clues(url):
    """Return a dictionary containing the clues and answers of the crossword from the given page"""
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    clue_list_p = soup.find("div", {"id":"clue_list"})

    clue_list = []
    for item in clue_list_p.find_all("p"):
        text = item.get_text()
        clue_list.extend(text.split("\n"))

    clue_list = list(filter(lambda x: x != "",clue_list)) # Remove empty string entry

    clues = {}
    for item in clue_list:
        item = item.lstrip('0123456789 ') # Remove number from front
        # Split clue and answer if separated with colon
        if (" : " in  item):
            item = item.split(" : ")
            store_clue(clues, item)
        elif (item.find("…") == 0):
            item = item.lstrip("…")
            if (item.find("..") != -1):
                item = item.split("..")
                store_clue(clues, item)
            elif (item.find("…") != 0):
                item = item.split("…")
                store_clue(clues, item)
        else: 
            print("Can't parse item: ", item)
    
    return clues

def write_to_csv(crossword_dict, file_name):
    # Make directory in file it is run in
    directory = "./data/"
    my_path = os.path.abspath(os.path.dirname(__file__))
    print(my_path)


# csv_file = date
# csvfile = open(csv_file + '.csv', 'wb')
# writer = csv.writer(csvfile)
# path = os.path.join(my_path, "./data/test.csv")
# with open(path) as f:
#     test = list(csv.reader(f))
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

    if (end_date < start_date):
        print("End date must be after or the same as the start date")
        sys.exit(0)

    # Generate dates
    date_range = generate_dates(args.start_date, args.end_date)

    base_url = "https://nyxcrossword.com"
    crossword = {}
    crosswords = {}
    for single_date in date_range:
        # print(single_date.strftime("%Y-%m-%d"))
        year = single_date.strftime("%Y")
        month = single_date.strftime("%m")
        day = single_date.strftime("%d")
        url_date_items = [year, month, day]
        
        url = urllib.parse.urljoin(base_url, ("/".join(url_date_items)))

        # clues_dict = get_clues(url)
        # crosswords[single_date.strftime("%Y-%m-%d")] = clues_dict
    if (args.start_date != args.end_date):
        file_name = "crossword-clues-from-" + str(args.start_date) + "-to-" + str(args.end_date) + ".csv"
    else: 
        file_name = "crossword-clues-on-" + str(args.start_date) + ".csv"
    print(file_name)
    # Write to csv
    write_to_csv(crosswords, file_name)
    # print(crosswords)
    #     urls.append(url)
    # print(urls)

main()


# try:
#     if not os.path.exists(directory):
#         os.makedirs(directory)
# except OSError:
#     print ('Error: Creating directory. ' +  directory)
    

# Example
# csv_columns = ['Date', 'Clue','Answer']

# names = name_pattern.findall("The basic idea of regular expressions is we define a pattern (the “regular expression” or “regex”) that we want to match in a text string and then search in the string to return matches. Some of these patterns look pretty strange because they contain both the content we want to match and special characters that change how the pattern is interpreted. Regular expressions come up all the time when parsing string information and are a vital tool to learn at least at a basic level!")
# print(clue_list)
#     if re.match("^[A-Za-z0-9_-]:", clue):
#         print(clue)
#     # do something here

# for linebreak in clue_list[0].find_all('br'):
#     linebreak.extract()
#     print(clue_list)
# clue_list = list(map(lambda x: x.text.split("<br/>"), clue_list))
# print(clue_list[0].)

# content = list(map(lambda x: x.text, clue_list))

# print(content)

# print(clue_list.prettify())

# write clue list to csv then graph data
#import pandas as pd
#daterange = pd.date_range(start_date, end_date)


#url = "https://nyxcrossword.com/"

#sp = "across_googlies"

#content = list(map(lambda x: x.text, tags))

#headers = requests.utils.default_headers()
#headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

#req = requests.get(url, headers)
#soup = BeautifulSoup(req.content, 'html.parser')
#print(soup.prettify())

# source 
# https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python

# https://stackoverflow.com/questions/42949449/using-pandas-date-range-to-generate-multiple-datetimes-two-dates-per-week
