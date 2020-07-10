#!/usr/bin/env python3
import os
import subprocess
import sys

import input_list_sanitiser
import online_definer


def run_OCR():
    '''Call imagestotxt-English.sh for a hardcoded directory.'''
    os.chdir('/home/simon/Projects/python/CEM-vocab-lister/pages')
    try:
        os.remove('binder.txt')
    except Exception as e:
        print(f'Problem deleting binder.txt: {e}')
    ocr = subprocess.run('imagestotxt-English.sh')
    os.chdir('/home/simon/Projects/python/CEM-vocab-lister')
    return ocr.returncode


def run_local_search(term):
    '''Check if a term has already been defined. Returns an existing
    definition.'''
    found = subprocess.run(
        ['rg', '--no-filename', f"^{term}",
         '/home/simon/Projects/python/CEM-vocab-lister/done/'],
        capture_output=True)

    if found.returncode == 0:
        found = found.stdout.decode('utf-8')
        found = found.split(":")[1].strip()
    else:
        found = ''

    return found


def main():

    if run_OCR() == 1:
        print("Could not run OCR. Exiting...")
        sys.exit(0)

    output_str = ''
    for word in input_list_sanitiser.remove_unwanted_word_fragments():

        definition = run_local_search(word)
        if len(definition) == 0:
            definition = online_definer.get_definition(word)

        output_str += f"{word}: {definition}\n"
        print(f"Added {word}: {definition}")

    with open('output.txt', 'w') as f:
        f.write(output_str)


if __name__ == '__main__':
    main()
