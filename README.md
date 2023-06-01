# Crawley

This script allows you to run crawlers and save the results in various formats.

# Installation

1.CLONE REPOSITORY:

 -git clone https://github.com/your/repository.git

2.INSTALL WITH POETRY:

Inside the Crawley directory, do:

 -poetry install
 
This will setup the enviroment to run the cli.

3.INSIDE CRAWLEY, YOU WILL RUN THE COMMAND:

 -python -m crawley.cli (Crawler) (argument) 
  
Available Crawlers:
- VultrCrawler
- HostgatorCrawler
  
Arguments:
- print
- save_json
- save_csv

Example: run "python -m crawley.cli VultrCrawler print"

This should print the required information crawled from vultr website.

4.TO SAVE A FILE IN JSON FORMAT, EXECUTE:

 -python -m crawley.cli (Crawler) (argument) --filename (output).json

You can choose the name of your file by switching in (output).

5.TO SAVE A FILE IN CSV FORMAT, EXECUTE:

 -python -m crawley.cli (Crawler) (argument) --filename (output).csv

You can choose the name of your file by switching in (output).

 That's the end of it. I hope this application can live up to 
the standards of good python Implementation.


