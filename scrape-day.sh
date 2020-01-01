# Usage: ./run-day.sh YYYY-mm-dd

python3.7 clue_list_scraper.py -s $1 -e $1 -l "$1.log"
echo "Scraping and generating csv for $1"