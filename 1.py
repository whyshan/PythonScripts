#!/bin/python

# Yue Chen

import re  # Import the regular expression library.

x = 0
y = []  # Initialize x and y

while x < 100:  # Loop over x = 1 to 100
    sent = raw_input('gimme a sentence: ')  # Ask for a sentence and store it in sent.
    if re.search('[A-Z]{2,5}$', sent):        # If there is 2 to 5 times of capital letters (e.g. POS tags) before EOL, do the following.
        sent = re.sub('[0-9]+\.[0-9]+', '<PAT1>', sent) # Replace any float number with <PAT1>.
        sent = re.sub('[A-Z][a-z]+ [A-Z][a-z]+ [~A-Z]', '<PAT2>', sent)        # # Replace a space, a capitalized word, a space, another capitalized word, a space and a not capitalized letter with <PAT2>.
        y += re.split('<PAT.>', sent)  # Split sent at <PAT1> and <PAT2>.
    x += 1  # Increase the counter.

print y  # Print list y.
