#!/bin/python

# Yue Chen

import string

punctuation = string.punctuation

# Read in by line and process

words = []
bigrams = []
frequency = {}
last = ""

blonde = open("blonde.txt", "r")

# Timer start -- begin
from time import clock

start = clock()
# Timer start -- end

for eachline in blonde:
    for char in eachline:
        if char in punctuation:
            eachline = eachline.replace(char, " " + char + " ")
            words = eachline.split()
            if len(words) < 1:
                break
            if (len(last) >= 1):
                bigrams.append([last, words[0]])
            for i in range(0, len(words) - 1):
                bigrams.append([words[i], words[i + 1]])
                last = words[-1]
print bigrams

# Statistic
for bigram in bigrams:
    bigram_string = str(bigram[0]) + " " + str(bigram[1])
    if frequency.has_key(bigram_string):
        frequency[bigram_string] += 1
    else:
        frequency[bigram_string] = 1
print frequency

# Timer end -- begin
finish = clock()
print finish - start
# Timer end -- end