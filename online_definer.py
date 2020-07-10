#!/usr/bin/env python3
import requests
import bs4
import sys


def get_definition(term):
    '''Returns (and tries to shorten to a sensible length) a definition
    for a given word.'''

    page = requests.get("https://kids.wordsmyth.net/we/?ent={}".format(term))

    try:
        page.raise_for_status()
    except Exception as e:
        print('There was a problem: %s' % (e))

    try:
        pageSoup = bs4.BeautifulSoup(page.content, "html.parser")

        row = pageSoup.find('tr', attrs={'class': 'definition'})

        definition = row.find('td', attrs={'class': 'data'}).getText()

        definition = definition.split('\n')[0]
        definition = definition.split('.')[0]
        definition = definition.split(';')[0]

        return definition

    except Exception as e:
        print(f'Problem looking up {term}: {e}')
        return "None found"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("You must supply an argument.")
        sys.exit(1)
    definition = get_definition(sys.argv[1])
    print(definition)
