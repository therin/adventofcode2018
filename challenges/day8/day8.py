# -*- coding: utf-8 -*-

import string

with open("input.txt") as file:
    input = [list(map(int, item.strip('\n').split(" ")))
             for item in file.readlines()]

input = input[0]

# first star

metadata = []


def buildTreeOne(input):
    if len(input) == 0:
        return 0
    childNodes = input.pop(0)
    metadataCount = input.pop(0)
    if childNodes > 0:
        for node in range(childNodes):
            buildTreeOne(input)
    else:
        pass
    if metadataCount > 0:
        for item in range(metadataCount):
            metadata.append(input.pop(0))


buildTreeOne(input[:])
print(sum(metadata))

# second star


class Node():
    """ Rerepsents a node in license file tree """

    def __init__(self, inputIterable):
        self.childCount = next(inputIterable)
        self.metadataCount = next(inputIterable)
        self.childNodes = [Node(inputIterable) for _ in range(self.childCount)]
        self.metadata = [next(inputIterable)
                         for _ in range(self.metadataCount)]


class Tree(object):
    """ Represents a tree built from license file """

    def __init__(self, input):
        self.root = Node(iter(node for node in input))


value = []


def getRootNodeValue(node):
    if node.childCount == 0:
        return value.append(node.metadata)
    else:
        for index in node.metadata:
            if (index - 1) >= len(node.childNodes):
                pass
            else:
                getRootNodeValue(node.childNodes[index - 1])


# first star
getRootNodeValue(Tree(input).root)
print(sum([sum(item) for item in value]))
