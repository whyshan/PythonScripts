#!/bin/python

# Yue Chen

# Read in by line and process

newvm = open("newvm.pos", "r")
results = []

# Timer start -- begin
from time import clock

start = clock()
# Timer start -- end
import re

pattern = re.compile(r'(\b\w+/DT\s\w+/JJ+\s\w+/NN| NNS)')

for eachline in newvm:
    match = pattern.findall(eachline)
    if match.__len__() > 0:
        results.append(match)

# print
for result in results:
    for match in result:
        print match

# Timer end -- begin
finish = clock()
print "time: ", finish - start, 's'
# Timer end -- end
