from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import datetime

web_url = "https://books.toscrape.com"

response = requests.get(web_url + "/index.html")
if response.status_code == 200:
    print("Successfully connected to the website.")
elif response.status_code == 403:
    print("Access forbidden.")
elif response.status_code == 404:
    print("Page not found.")
else:
    print("Failed to connect.")

books_soup = BeautifulSoup(response.text, 'html.parser')

def remove_char(string, ch):
    found = string.find(ch)
    if found > 0:
        return string[:found]
    return string

w_to_d = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

all_books = []

count = 1
while True:
    response = requests.get(web_url + '/catalogue/' + "page-{}.html".format(count))
    if response.status_code == 200:
        count += 1
    else:
        break

for page_number in range(1, count):
    page_url = web_url + '/catalogue/' + "page-{}.html".format(page_number)
    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.text, 'html.parser')
    
    all_articles = page_soup.find_all('article', class_='product_pod')

    for index, article in enumerate(all_articles, start=1):
        scraping_date = datetime.date.today()

        b_href_partial = article.find('a')['href']
        b_href = f"{web_url}/{b_href_partial}"

        b_title = article.find('h3').find('a')['title']
        b_title = remove_char(b_title, '(').strip()
        b_title = remove_char(b_title, ':').strip()

        rating_classes = article.find('p', class_='star-rating')['class']
        b_rtg = rating_classes[1] if len(rating_classes) > 1 else 'No Rating'
        b_rtg_num = w_to_d.get(b_rtg, 0)

        b_price = article.find('p', class_='price_color').text.strip()
        b_price = re.sub(r'[^\d.]+', '', b_price) 
        b_price_value = float(b_price)

        b_stock = article.find('p', class_='instock availability').text.strip()

        res = requests.get(b_href)
        one_book_url = BeautifulSoup(res.text, 'html.parser')

        p_categ_element = one_book_url.find("a", href=re.compile("../category/books/"))
        if p_categ_element:
            p_categ = p_categ_element.get("href").split("/")[3]
            p_categ = re.sub(r'_\d+', '', p_categ) 
        else:
            p_categ = "N/A" 

        p_avail_element = one_book_url.find("p", class_="instock availability")
        if p_avail_element:
            p_avail_text = p_avail_element.text
            p_avail = int(re.search(r'\d+', p_avail_text).group())
        else:
            p_avail = 0 

        p_ups_element = one_book_url.find("td")
        if p_ups_element:
            p_ups = p_ups_element.text.strip()
        else:
            p_ups = "N/A" 
            
        all_books.append([scraping_date, b_title, b_href, b_rtg_num, b_stock, b_price, p_categ, p_avail, p_ups])

        print(f"Processed book {index} on page {page_number}")


df = pd.DataFrame(all_books, columns=['Date', 'Title', 'URL', 'Rating', 'Stock', 'Price', 'Category', 'Availability', 'UPC'])
df.to_csv('books_catalog.csv', index=False)

print("Data collection completed!")
