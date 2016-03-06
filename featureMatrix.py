#!/bin/python

# Professor Sandra Kuebler
# Apply ML Techniques in CL
# Yue Chen, Hai Hu and Eriya Terada
# March 13th, 2016

# minidom
from xml.dom import minidom

# Define wordClass
class wordClass:
	def __init__(self, instanceId, senseId, context):
		self.instancdId = instanceId
		self.sensId = senseId
		self.context = context

# Open the files and read in the data
def openRead(fileName):
#	rawFile = open(fileName)
#	newLine = "whatsoever"
#	while newLine:
#		newLine = rawFile.readline()
	parsedFile = minidom.parse(fileName)
	instanceList = parsedFile.getElementsByTagName("instance")
	instance


# Main

# Open the files and read in the data
fileName = raw_input(" ")
openRead(fileName)

# Extract context features
contextFeature = extractContextFeature(wordClass)

# Create feature matrix
featureMatrix = createFeatureMatrix(contextFeature)
