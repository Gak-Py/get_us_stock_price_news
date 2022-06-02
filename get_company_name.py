import requests
from bs4 import BeautifulSoup
def get_company_name(name):
    target_url=f"https://stocks.finance.yahoo.co.jp/us/profile/{name}"
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    company_name = soup.select("#main > div.padT6.marB10 > div > table > tr:nth-child(2) > td")
    company_name_str = company_name[0]
    f_company_name = company_name_str.text.replace("<td>", "")
    return f_company_name

