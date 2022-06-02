from get_company_name import get_company_name
import requests
#dotenv-templete
import os
import datetime as dt
from dotenv import load_dotenv
from os.path import join, dirname
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
#dotenv-templete

STOCK_NAME = input("Type Company Code eg.TSLA : ")
STOCK_API = os.getenv("STOCK_API")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API = os.getenv("NEWS_API")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


today_news = dt.datetime.today()
today_news = today_news.strftime("%Y-%m-%d")

company_name = get_company_name(STOCK_NAME)
print(company_name)

def get_stock_price():
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API,
    }
    url = STOCK_ENDPOINT
    r = requests.get(url, params=params)
    data = r.json()["Time Series (Daily)"]
    data_list = [value for (key,value) in data.items()]
    today_data = float(data_list[0]["4. close"])
    yesterday_data = float(data_list[1]["4. close"])

    if today_data <= yesterday_data * 0.9:
        print("OMG! why?")
        get_stock_news()
    else:
        print("Keep it!")

def get_stock_news():

    params = {
        "q": company_name,
        "from": today_news,
        "apikey": NEWS_API,
        "language": "en",
        "searchIn": "title",
    }
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    if data["articles"] == []:
        print("no news...")
    else:
        article_source = data["articles"][0]["source"]["name"]
        article_title = data["articles"][0]["title"]
        article_url = data["articles"][0]["url"]
        print(f"{article_source} : {article_title} - {article_url}")

get_stock_price()
