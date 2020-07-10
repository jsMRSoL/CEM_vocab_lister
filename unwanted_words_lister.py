#!/usr/bin/env python3
import csv

i = 0
unwanted_words = dict()

with open('corpus-data/cleaned1.txt', 'r', encoding="ISO-8859-1") as f:
    words_list = csv.DictReader(f, delimiter='\t')

    for item in words_list:
        if item['Freq'] is not None:
            unwanted_words[int(item['Freq'])] = item['Word']

for k in sorted(unwanted_words.keys()):
    print(f"Word:\t{unwanted_words[k]}\t\tRank:{k}")
    i += 1
    if i == 10:
        break
