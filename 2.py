#!/bin/python

# Yue Chen

#words = {}
words = [] # Error 1: words should be a list instead of a dictionary.
#for x < 50:
for x in range(0,50): # Error 2: Wrong syntax for for loop.
	words.append(raw_input('next word: '))
#words.sorted()
words.sort() # Error 3: .sort() is the right method to sort a list.
#for x in range (1,50):
for x in range(1,51): # Error 4: The range should cover the last word.
#	print words[x], ’words to do:’, 50-x
	print words[x-1], 'words to do:', 50-x # Error 5: The list counts from 0.
