# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:02:37 2018

@author: Gabriel

"""

import bibtexparser
import pandas as pd

data = pd.read_csv('SearchResults_IEEE.csv', encoding='utf-8')


with open('search_IEEE.bib', encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
    
    
for entry in bib_database.entries:
    dado = data.loc[data['DOI'] == entry['doi']]
    abstract = dado['Abstract'].item()
    entry['Abstract'] = abstract
     

with open('search_IEEE.bib', 'w', encoding="utf-8") as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)