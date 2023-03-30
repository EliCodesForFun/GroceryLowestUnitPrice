
# TODO 
# Need to change the order of some of the code here, was running with Jupyter Noteb
# Add a CLI to scrape a site for lowest price.
# Make this more modular so that 

###ShopRite Scraper lol
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

site = r'https://www.shoprite.com/sm/pickup/rsid/3000/results?q=chicken%20breast'
driver.get(site)
shop_rite_html = driver.page_source
print(shop_rite_html)



shop_rite_html = ""
with open("shopritetemp.html", encoding='utf-8') as file:
    for line in file:
        print(line)
        shop_rite_html += line
print(shop_rite_html)


import pprint

response = requests.get(site)
pprint.pprint(response.text)

soup = BeautifulSoup(shop_rite_html, "html.parser")
print(soup.prettify())
all_unit_prices = soup.find_all(class_="ProductUnitPrice--slbqgg iydwJZ")
print(all_unit_prices) 

item_names = []
for item in all_unit_prices:
    item_names.append(item.parent.previous_sibling.previous_sibling.text)

item_prices = []
for item in all_unit_prices:
    item_prices.append(item.text)

units = []
prices = []
for item in item_prices:
    prices.append(item.split(sep=r'/')[0])
    units.append(item.split(sep=r'/')[1])
print(units)
print(prices)

prices_df = pd.DataFrame({
    "Prices": prices,
    "Units": units,
    "Names": item_names
})
prices_df.Prices = prices_df.Prices.str.replace("$", "").astype(float)


temp_df = prices_df.sort_values(["Prices", "Units"])
temp_df

prices_df.prices.min()