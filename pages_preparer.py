#!/usr/bin/env python3

import os
import subprocess


def run_local_search(term):
    found = subprocess.run(
        ['rg', '--no-filename', f"^{term}",
         '/home/simon/Projects/python/CEM-vocab-lister/done/'],
        capture_output=True)

    return found.stdout.decode('utf-8')


print(run_local_search('determined'))
