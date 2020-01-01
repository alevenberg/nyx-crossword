# Crossword

This is a python script that scrapes [this site](https://nyxcrossword.com/) for crossword answers in a given date range.

## Setup

1. Setup your virtual environment
    - For mac OS: `python3 -m venv env`

2. Activate your virtual environment: `source ./env/bin/activate`

3. Install requirements.txt: `pip3 install -r requirements.txt`

4. Run the scrape.py script: `python3 scrape.py -s 2019-10-01 -e 2019-10-31 -l october.log`
    - Note: you can run the script with the same start and end date it will scrape the clues for that day

5. The csv file will be found in `./data/crossword-clues-from-2019-10-01-to-2019-10-31.csv`

6. When finished running the script
    - You can deactivate your virtual environment: `deactivate`
    - You can also delete the log files and data directory by running a cleaning script
        - Give execute permissions: `chmod 755 clean.sh`
        - Run script: `./clean.sh`
