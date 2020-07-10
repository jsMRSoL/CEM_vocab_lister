#!/usr/bin/env python3
import nltk


def remove_unwanted_word_fragments():
    '''Remove unwanted words and fragments from a text file.
    Requires nltk.'''

    # Create a set of words for reference
    words = set(nltk.corpus.words.words())

    # Remove common words from the tests and common fragments from OCR
    words.difference_update(set(['dis', 'y', 'ly', 'h', 'select', 'most',
                                 'appropriate', 'word', 'table', 'complete',
                                 'pair', 'synonym', 'antonym', 'below',
                                 'corresponding', 'line', 'accurately',
                                 'underline', 'brackets', 'complete', 'mark',
                                 'ton', 'an', 'is', 'was', 'I']))

    # Remove the commonest 1000 words
    unwanted_words = set()
    with open('unwanted_words.txt', 'r') as f:
        for i in range(1000):
            unwanted_words.add(f.readline().split()[0])
    words.difference_update(unwanted_words)

    # Get the test text for cleaning
    with open('pages/binder.txt', 'r') as f:
        text = f.read()

    # Make a set of recognisable words from the input file
    clntext = {w for w in nltk.wordpunct_tokenize(text)
               if w.lower() in words}
    clntext.discard('I')

    return clntext


if __name__ == '__main__':

    clntext = remove_unwanted_word_fragments()
    print(clntext)
    print(len(clntext))
