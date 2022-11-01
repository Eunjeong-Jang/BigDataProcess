#!/usr/bin/python3
import sys

movieDict = dict()
inputFile = sys.argv[1]
outputFile = sys.argv[2]

with open(inputFile, "rt") as fp:
	for line in fp:
		line = line[:-2]
		movie = line.split("::")
		genre = movie[2].split("|")
		print(genre)
		for g in genre:
			if g not in movieDict:
				movieDict[g] = 1
			else:
				movieDict[g] += 1

with open(outputFile, "wt") as fp:
	for m in movieDict:
		fp.write(m + " " + str(movieDict[m]) + "\n")

with open(outputFile, "rt") as fp:
	for line in fp:
		print(fp.read())
