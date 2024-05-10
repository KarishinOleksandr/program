import bs4
import requests

url = 'https://www.python.org/'
reqs = requests.get(url)
print(reqs)
soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

urls = []
for h in soup.find_all('li'):
    a = h.find('a')
    urls.append(a.attrs['href'])
print(urls)

h2_tags = soup.find_all('h2')
print("First ten h2 tags on python.org:")
for index, h2_tag in enumerate(h2_tags[:10], start=1):
    print(f"{index}. {h2_tag.text.strip()}")

header_tags = []
for header_level in ['h1', 'h2', 'h3']:
    headers = soup.find_all(header_level)
    for header in headers:
        header_tags.append((header.name, header.text.strip()))

print("List of h1, h2, h3 tags and their text values from python.org:")
for tag_name, text_value in header_tags:
    print(f"Tag: {tag_name}, Text: {text_value}")


unique_tags = set()
tags_count = {}

for child in soup.recursiveChildGenerator():
    if child.name:
        tag_name = child.name
        unique_tags.add(tag_name)
        if tag_name in tags_count:
            tags_count[tag_name] += 1
        else:
            tags_count[tag_name] = 1

print("Unique HTML tags:")
for tag in sorted(unique_tags):
    print(tag)

print("\nTag counts:")
for tag, count in tags_count.items():
    print(f"{tag}: {count}")


root = soup.html

root_childs = [e.name for e in root.children if e.name is not None]

print("Child elements of <html> tag:")
print(root_childs)


li_tags = soup.find_all('li')

print("All <li> tags found on the webpage:")
for li_tag in li_tags:
    print(li_tag)


elements_with_python = soup.find_all(string=lambda text: 'Python' in str(text))

for element in elements_with_python:
    print(element)


formatted_html = soup.prettify()

print(formatted_html)