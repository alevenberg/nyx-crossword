# Usage: ./run-year.sh YYYY
# Currently only works for 2019

python3.7 scraper.py -s $1-01-01 -e $1-12-31 -l "$1.log"
echo "Scraping and generating csv for the year $1"