# GroceryLowestUnitPrice
This is a Python-based web scraper that will be able to scrape the grocery unit prices for various websites.

I started it with Shop Rite, a grocery store that is popular in Philadelphia.
Looking to turn this into a CLI that can take various websites and use the appropriate webscraper and parser.

Currently it works, but you must have Selenium and the setup on your computer.
This uses the code `driver = webdriver.Chrome()` so you might not need the Chromedriver thing:

Download:
https://chromedriver.chromium.org/downloads
Add the .exe to your environmental variables

`pip install selenium`



Ideally, usage might look like this

`python GroceryLowestUnitPrice.py -u shoprite.com -i Broccoli`

`python GroceryLowestUnitPrice.py -s Shop_Rite -i Broccoli`

`python GroceryLowestUnitPrice.py -u shoprite.com/url/to/item`


The result would be URLs for the top 3 items by $/oz and $/lb.
Should be able to implement $/ct as well for this like napkins, paper towels, etc.
