#!/usr/bin/python3
import sys
import calendar

dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
uberDic1 = dict()
uberDic2 = dict()
inputFile = sys.argv[1]
outputFile = sys.argv[2]

with open(inputFile, "rt") as fp:
	for line in fp:
		info = line.split(",")

		info_date = info[1].split("/")
		day = calendar.weekday(int(info_date[2]), int(info_date[0]), int(info_date[1]))
		string = info[0] + "," + dayofweek[day]
		if string not in uberDic1:
			uberDic1[string] = int(info[2]) 
			uberDic2[string] = int(info[3])
		else:
			uberDic1[string] += int(info[2])
			uberDic2[string] += int(info[3])

with open(outputFile, "wt") as fp:
	for line in uberDic1:
		fp.write(line + " " + str(uberDic1[line]) + "," + str(uberDic2[line]) + "\n")
