# Crawley

This project allows you to run crawlers and save the results in various formats.

# Installing and Running

## 1. Clone Repository

- git clone https://github.com/your/repository.git

## 2. Install with Poetry

### Inside the Crawley directory, do:

- poetry install

To install the enviroment via poetry.

### Then, do:
 
- poetry shell

To activate the virtual enviroment.

### This will setup the enviroment to run the cli.

## 3. Running Crawley

### Available Crawlers:

- VultrCrawler
- HostgatorCrawler
  
### Arguments:

- print
- save_json
- save_csv

### Inside Crawley, you will run the command:
 
 -python -m crawley.cli (Crawler) (argument) 
  

### To print the required information crawled from the website: 

- python -m crawley.cli (Crawler) print"

This should print the required information crawled from the website.

### To save file in .json, execute:

- python -m crawley.cli (Crawler) (argument) --filename (output).json

The .json file will be saved in the current directory

* You can choose the name of your file by switching in (output).

### To save a file in .csv, execute:

- python -m crawley.cli (Crawler) (argument) --filename (output).csv

The .csv file will be saved in the current directory

* You can choose the name of your file by switching in (output).

## Final Note

That's the end of it. I hope this application can live up to 
the standards of good python Implementation.


