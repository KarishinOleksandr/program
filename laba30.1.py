import requests
from bs4 import BeautifulSoup
import pandas as pd

exchange_rates = []

def parse_rates_privatbank(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    currency_pairs = soup.find_all('div', class_='currency-pairs')

    printed_currencies = {}

    for currency_pair in currency_pairs:
        names = currency_pair.find('div', class_='names').text.strip().split()[0]

        purchase_element = currency_pair.find('div', class_='purchase')
        purchase = purchase_element.text.strip() if purchase_element and purchase_element.text.strip() != '' else 'N/A'

        sale_element = currency_pair.find('div', class_='sale')
        sale = sale_element.text.strip() if sale_element and sale_element.text.strip() != '' else 'N/A'

        if names not in printed_currencies:
            printed_currencies[names] = True
            exchange_rates.append({
                'Bank': 'PrivatBank',
                "Currency:": names,
                "Purchase:": purchase,
                "Sale:": sale
            })

def parse_rates_pumb(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('div', class_='exchange-rate')

    if table:
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')

            if len(cells) >= 3:
                currency = cells[0].text.strip()
                purchase = cells[1].text.strip()
                sale = cells[2].text.strip()

                exchange_rates.append({
                'Bank': 'PUMB',
                'Currency:': currency,
                'Purchase:': purchase,
                'Sale:': sale
            })


def parse_rates_sensebank(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Не вдалося отримати сторінку")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='exchange-rate-tabs__item')

    for item in items:
        currency_name_div = item.find('div')
        currency_name = ""
        if currency_name_div:
            if currency_name_div.find('span'):
                currency_name = currency_name_div.find('span').text.strip()
            elif currency_name_div.find('h2'):
                currency_name = currency_name_div.find('h2').text.strip()
        
        if currency_name:
            if currency_name == "UAH":
                currency_name = "USD"
            elif currency_name == "USD":
                currency_name = "EUR/USD"

            info_blocks = item.find_all('div', class_='exchange-rate-tabs__info-item')
            if len(info_blocks) >= 2:
                purchase = info_blocks[0].find('h3').text.strip()
                sale = info_blocks[1].find('h3').text.strip()

                if float(purchase) > 43:
                    currency_name = "EUR"

                exchange_rates.append({
                'Bank': 'SenseBank',
                'Currency:': currency_name,
                'Purchase:': purchase,
                'Sale:': sale
                          })

def parse_rates_poltavabank(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'footable_5065'})

    rows = table.find('tbody').find_all('tr')

    for row in rows:
        columns = row.find_all('td')
        if len(columns) == 3:
            currency_name = columns[0].text.strip()
            purchase = columns[1].text.strip()
            sale = columns[2].text.strip()

            exchange_rates.append({
                'Bank': 'PoltavaBank',
                'Currency:': currency_name,
                'Purchase:': purchase,
                'Sale:': sale
                          })

urls = {
    'PrivatBank': 'https://privatbank.ua/rates-archive#online-block',
    'PUMB': 'https://about.pumb.ua/info/currency_converter',
    'SenseBank': 'https://sensebank.ua/currency-exchange',
    'PoltavaBank': 'https://poltavabank.com/'
}

for bank_name, url in urls.items():
    try:
        if bank_name == 'PrivatBank':
            parse_rates_privatbank(url)
        elif bank_name == 'PUMB':
            parse_rates_pumb(url)
        elif bank_name == 'SenseBank':
            parse_rates_sensebank(url)
        elif bank_name == 'PoltavaBank':
            parse_rates_poltavabank(url)
    except Exception as e:
        print(f"Error parsing {bank_name}: {e}")

df = pd.DataFrame(exchange_rates)
df.to_csv('exchange_rates.csv', index=False, encoding='utf-8')