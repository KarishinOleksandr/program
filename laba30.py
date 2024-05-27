import requests
from bs4 import BeautifulSoup

url = 'https://www.x-rates.com/calculator/?from=GBP&to=USD&amount=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

part1 = soup.find(class_='ccOutputTrail').previous_sibling
part2 = soup.find(class_='ccOutputTrail').get_text(strip=True)
rate = float(f"{part1}{part2}")

print("Current exchange rate GBP to USD:", rate)

def gbp_to_usd(rate, gbp):
    dolr = gbp * rate
    return dolr

gbp_amount = float(input("Enter amount in GBP: "))
usd_amount = gbp_to_usd(rate, gbp_amount)

print(f"{gbp_amount} GBP is {usd_amount:.2f} USD")
