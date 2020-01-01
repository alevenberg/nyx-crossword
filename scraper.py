from bs4 import BeautifulSoup
import requests
import re
import csv
import os
import os.path
import csv 
import argparse
import datetime

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

print(args.start_date)
print(args.end_date)

def generate_dates(start_date, end_date):

nyx_url = "https://nyxcrossword.com/2019/11/01"

def get_clues(url):
    """Return a dictionary containing the clues and answers of the crossword that day"""
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
        item = re.split(' : ', item) # Split clue and answer
        key = item[0]
        answer = item[1]
        clues[key] = answer
    return clues

crossword = {}


def main():
    print("running!")
main()
# Make directory in file it is run in
# directory = "./data/"
# my_path = os.path.abspath(os.path.dirname(__file__))
# print(my_path)

# csv_file = date
# csvfile = open(csv_file + '.csv', 'wb')
# writer = csv.writer(csvfile)
# path = os.path.join(my_path, "./data/test.csv")
# with open(path) as f:
#     test = list(csv.reader(f))

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
