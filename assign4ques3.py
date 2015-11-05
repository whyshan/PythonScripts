#!/bin/python

# Yue Chen

import string

punctuation = string.punctuation

# Read in by line and process

words = []
bigrams = []
last = ""

blonde = open("blonde.txt","r")
for eachline in blonde:
	for char in eachline:
		if char in punctuation:
			eachline = eachline.replace(char, " " + char + " ")
			words = eachline.split()
			if len(words) < 1:
				break
			if (len(last) > 1):
				bigrams.append([last, words[0]])
			for i in range(0, len(words)-1):
				bigrams.append([words[i], words[i+1]])
				last = words[-1]
