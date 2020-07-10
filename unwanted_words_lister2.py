#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests

unwanted_words = dict()

page = requests.get("https://www.wordfrequency.info/free.asp?s=y")

try:
    page.raise_for_status()
except Exception as e:
    print('Could not get page.')

pageSoup = bs(page.content, "html.parser")

tables = pageSoup.findAll('table', id='table1')

rows = tables[2].findAll('tr')

for row in rows:
    data = row.findAll('td')
    rank = data[0].getText()
    word = data[1].getText()
    try:
        unwanted_words[int(rank)] = word
    except Exception as e:
        print(f'{rank} caused a problem...')

i = 0
for k in sorted(unwanted_words.keys()):
    print(f"Word:\t{unwanted_words[k]}\t\tRank:{k}")
    i += 1
    if i == 10:
        break

file_contents = ''
for k in sorted(unwanted_words.keys()):
    file_contents += f"{unwanted_words[k]}\t{k}\n"

with open('unwanted_words.txt', 'w') as f:
    f.write(file_contents)
