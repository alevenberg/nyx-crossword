# Usage: ./run-year.sh YYYY

python3.7 clue_list_scraper.py -s $1-01-01 -e $1-12-31 -l "$1.log"
echo "Scraping and generating csv for the year $1"