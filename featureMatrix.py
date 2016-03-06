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
	
	xmlDoc = minidom.parse(fileName)

	instanceList = xmlDoc.getElementsByTagName('instance')
	print(len(instanceList))
	for instance in instanceList:
    	print(instance.attributes['id'].value)

	answerList = xmlDoc.getElementsByTagName('answer')
	print(len(answerList))
	for answer in answerList:
    	print(answer.attributes['senseid'].value)

	contextList = xmlDoc.getElementsByTagName('context')
	print(len(contextList))
	for context in contextlist:
   		print(context.firstChild.nodeValue)

   	i = 0
   	wordClassList = []
   	while i < len(instanceList):
   		wordClassList[i].wordClass(instancelist[i].attributes['id'].value， answerlist[i].attributes['senseid'].value， contextlist[i].firstChild.nodeValue)
   		i += 1

   	return wordClassList

# Extract context features
def extractContextFeature(wordClassList):
	
	i = 0
	contextFeature = ""
	while i < len(wordClassList):
		contextFeature += wordClassList[i].context
		i += 1

	contextFeature.split(" ")
	
	contextFeature = list(set(contextFeature))

	return contextFeature


# Main

# Open the files and read in the data
fileName = raw_input(" ")
wordClassList = openRead(fileName)

# Extract context features
contextFeature = extractContextFeature(wordClassList)

# Create feature matrix
featureMatrix = createFeatureMatrix(contextFeature)
