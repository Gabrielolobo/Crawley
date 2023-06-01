# Crawley

This script allows you to run crawlers and save the results in various formats.

# Installation

1.Clone the Repository:

 -git clone https://github.com/your/repository.git

2.Install with poetry:

Inside the Crawley directory, do:

 -poetry install
 
This will setup the enviroment to run the cli.

3.Inside Crawley, you will run the command:

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

To save a file in json format, execute:

 --python -m crawley.cli (Crawler) (argument) --filename (output).json

You can choose the name of your file by switching in (output).


