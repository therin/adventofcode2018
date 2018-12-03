# -*- coding: utf-8 -*-
from collections import defaultdict

# load input file
with open("input.txt") as file:
    input = [line.strip("\n") for line in file.readlines()]

# build a 2d array with fabric size
fabric = [[0 for x in range(1000)] for y in range(1000)]

# helper function to get indices to mark
def getIndices(claim):
    indicesToMark = []
    # extract initial coordinates (coverts to 0-indexed array addressing)
    coordinates = [int(x)  for x in claim.split(" ")[2].strip(":").split(",")]
    # extract size
    size = [int(x) for x in claim.split(" ")[3].split("x")]
    # loop over size and populate toMark list
    for i in range(coordinates[0], coordinates[0]+size[0]):
        for j in range(coordinates[1], coordinates[1]+size[1]):
            indicesToMark.append((j,i))

    return indicesToMark

# apply claims
overlapDict = defaultdict(list)
for index, item in enumerate(input):
        # extract claim id
        claimId = int(item.split(" ")[0].strip("#"))
        for i,j in getIndices(item):
                overlapDict[(i,j)] += [claimId]

# count overlapping items
print(sum(len(v) > 1 for v in overlapDict.values()))

# second star
# build a full list of claims
allClaims = {*range(1, int(input[-1].split(" ")[0].strip("#"))+1)}
# loop over all claimed areas and remove those with more then one overlap
for item in overlapDict.values():
    if len(item) > 1:
        allClaims -= {*item}

print(allClaims)


