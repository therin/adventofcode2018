# -*- coding: utf-8 -*-

# Load input file

with open("input.txt") as file:
	input = [line.strip("\n") for line in file.readlines()]


# Convert to set and use it as input to count()
counterTwo = 0
counterThree = 0

# Part one
# Count two's
for item in input:
	for letter in set(item):
		if item.count(letter) == 2:
			counterTwo += 1
			break

# Count three's

for item in input:
	for letter in set(item):
		if item.count(letter) == 3:
			counterThree += 1
			break

print(counterTwo * counterThree)


# Part two
differenceCounter = 0
singleDiffIds = []
currentCounter = 0

for indexX, item in enumerate(input):
		for indexY, anotherItem in enumerate(input):
				currentCounter = 0
				zippedTuples = zip(item,anotherItem)
				# go over zipped tuples and count diffrences
				for i,j in zippedTuples:
					if i != j:
						currentCounter += 1
					if currentCounter > 1:
						break
				if currentCounter == 1:
						singleDiffIds.append((item, anotherItem))


print(singleDiffIds[0])


