#!/usr/bin/env python
import sys
import string

stopwards = set(['the', 'and'])

#create translator for mapping punctuation to whitespace
translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    line = line.translate(translator)
    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
       if word not in stop_words:
           print '%s\t%s' % (word, "1")
