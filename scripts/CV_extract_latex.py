#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

input = "./print/index.html"
print()
# Extract relevant part of the page
soup = BeautifulSoup(open(input), 'html.parser')
CV_tex = soup.find('code').text

# Translate html escape to latex escape
escape_characters = {'&percnt'  : '\%',
                     '&amp;'    :'\&',
                     '&gt;'     : '>',
                     '&lt;'     : '<',
                     '[:tab:]'  : '&'}
CV_tex_clean = CV_tex
for htmlesc, latexesc in escape_characters.items():
    print('Substitute', htmlesc, 'to', latexesc)
    CV_tex_clean = CV_tex_clean.replace(htmlesc, latexesc)

# Write the output to tex file
file = open('./files/CV_Hanno_Kase.tex', 'w')
file.write(CV_tex_clean)
file.close()
