#!/usr/bin/env python3

import json
import copy

def read_ipynb(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_ipynb(notebook, notebook_path):
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f)


first_notebook = read_ipynb('1 - Analyse du jeu de données.ipynb')
second_notebook = read_ipynb('2 - Classification.ipynb')
final_notebook = copy.deepcopy(first_notebook)
final_notebook['cells'] = first_notebook['cells'] + second_notebook['cells']
# Saving the resulting notebook
write_ipynb(final_notebook, 'Rapport Data Mining 2.ipynb')