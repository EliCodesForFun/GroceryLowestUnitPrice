# GroceryLowestUnitPrice
This is a Python-based web scraper that will be able to scrape the grocery unit prices for various websites.

I started it with Shop Rite, a grocery store that is popular in Philadelphia.
Looking to turn this into a CLI that can take various websites and use the appropriate webscraper and parser.

Ideally, usage might look like this

python GroceryLowestUnitPrice.py -u shoprite.com -i Broccoli

python GroceryLowestUnitPrice.py -s Shop_Rite -i Broccoli

python GroceryLowestUnitPrice.py -u shoprite.com/url/to/item


The result would be URLs for the top 3 items by $/oz and $/lb.
Should be able to implement $/ct as well for this like napkins, paper towels, etc.
