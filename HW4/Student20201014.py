#!/usr/bin/python3
import sys
import os
import numpy as np
import operator

training = sys.argv[1]
test = sys.argv[2]

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	#print(dataSetSize)
	#print(inX)
	#print(dataSet)
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	#print(diffMat)
	sqDiffMat = diffMat ** 2
	#print(sqDiffMat)
	sqDistances = sqDiffMat.sum(axis = 1)
	#print(sqDistances)
	#distances = sqDistances ** 0.5
	sortedDistIndicies = sqDistances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(),
		key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

os.chdir("./" + training)
trainingList = os.listdir()
labels = []
group = []
for t in range(len(trainingList)):
	filename = trainingList[t]
	N = filename[0]
	labels.append(N)
	
	dataList = []
	with open(filename, "rt") as f:
		for line in f:
			data = []
			for one in line:
				if one != '\n':
					data.append((int)(one))
			dataList.extend(data)
	group.append(dataList)

#print(group)
npGroup = np.array(group)
	
os.chdir("../" + test)
testList = os.listdir()
for i in range(1, 21):
	wrongAnswer = 0
	for t in range(len(testList)):
		filename = testList[t]

		data = []
		with open(filename, "rt") as f:
			for line in f:
				for one in line:
					if one != '\n':
						data.append((int)(one))

		returnValue = classify0(data, npGroup, labels, i)
		if filename[0] != returnValue:
			wrongAnswer += 1
	errorRate = wrongAnswer / len(testList) * 100
	print("%.0f" % errorRate)
	#print(errorRate)
