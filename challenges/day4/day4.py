# -*- coding: utf-8 -*-

from collections import defaultdict
import datetime
import re

regex = r"\[(.*?)\]"

# load input file
with open("input.txt") as file:
    input = [line.strip("\n") for line in file.readlines()]

# extract data
regex = r"\[(.*?)\]"
input = [(re.search(regex, i).group(1), i.partition("]")[2].lstrip()) for i in input]
input = sorted(input, key=lambda x: x[0])


def extractGuardID(item):
	if "Guard #" in item[1]:
		guardID = item[1].split(" ")[1].lstrip("#")
		return (True, guardID)
	else: 
		return (False, 0)


guardSleep = defaultdict(int)
minuteCounter = defaultdict(int)

for index, event in enumerate(input):
	if extractGuardID(event)[0]:
		currentIndex = index + 1
		currentGuard = extractGuardID(event)[1]
	else:
		if "falls asleep" in event[1]:
			fellAsleep = int(input[index][0][14:17])
			wokeUp = int(input[index+1][0][14:17])
			guardSleep[currentGuard] += wokeUp - fellAsleep
			for minute in range(fellAsleep,wokeUp):
				minuteCounter[(currentGuard,minute)] += 1

maxGuardSleep = sorted(guardSleep.items(), key=lambda x: x[1])[-1]
filteredMinuteDict = {k:v for k,v in minuteCounter.items() if k[0] == maxGuardSleep[0]}
print(sorted(filteredMinuteDict.items(), key=lambda x: x[1]))

# part two
print(sorted(minuteCounter.items(), key=lambda x: x[1]))

