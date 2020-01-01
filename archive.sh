for (( i=2012; i<=2019; i++ ))
do  
    echo "Scraping for $i"
    python3.7 clue_list_scraper.py -s $i-01-01 -e $i-12-31 -l "$i.log"
    python3.7 analysis.py -s $i-01-01 -e $i-12-31
    python3.7 graph.py -s $i-01-01 -e $i-12-31
done
