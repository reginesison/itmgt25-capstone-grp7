from bs4 import BeautifulSoup
import requests

url_link = "https://www.theglobaleconomy.com/rankings/stock_market_capitalization_dollars/"
result = requests.get(url_link)
html = result.text
soup = BeautifulSoup(html, features="lxml")

tds = soup.find_all('td')
size = 4

tempList = []
for td in tds:
    tempList.append(td.text.strip())

finalList = [tempList[n:n+size] for n in range(0, len(tempList), size)]
for item in finalList:
    print((item[0] + "'s stock market value is at $" + item[1] + " in 2020 and is in rank #" + item[2] + "."))