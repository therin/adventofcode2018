# -*- coding: utf-8 -*-

# Load input file

with open("input.txt") as file:
	input = [int(line) for line in file.readlines()]

# first
current = 0 

for number in input:
	current += number
	
print(current)

# second
found = False
current = 0
currentSet = set()

while True:
	for number in input:
		current += number
		# print("Searching {} in {}".format(current, currentSet))
		if current in currentSet:
			print("Found {}".format(current))
			found = True
			break
		currentSet.add(current)
	if found:
		break


