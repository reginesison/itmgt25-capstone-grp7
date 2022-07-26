from flask import Flask, render_template, request, flash
app = Flask(__name__)
from bs4 import BeautifulSoup
import requests

app.secret_key = "itm_is_fun<333"

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
    answer = str((item[0] + "'s stock market value is at $" + item[1] + " in 2020 and is in rank #" + item[2] + "."))

@app.route("/stock", methods=['POST', 'GET'])
def index():
    flash("What is the stock market value in this country?")
    return render_template("index.html",answer=answer)

@app.route("/show", methods=['POST', 'GET'])
def show():
    flash(answer)
    return render_template("index.html",answer=answer)