# -*- coding: utf-8 -*-

import networkx as nx
import string

with open("input.txt") as file:
    input = [item.strip('\n').split(" ") for item in file.readlines()]


def buildGraph(input):
    graphTuples = []

    for item in input:
        graphTuples.append((item[1], item[7]))

    graph = nx.DiGraph()

    for edge in graphTuples:
        graph.add_edge(edge[0], edge[1])

    return graph


steps = ''

graph = buildGraph(input)

while graph:
    # Return the in-degree of a node or nodes.
    # The node in-degree is the number of edges pointing in to the node.
    # find calculate vertex without inbound edges
    next_step = min([n for n, d in graph.in_degree if d == 0])
    steps += next_step
    graph.remove_node(next_step)

print(steps)


# second star

class Pool():
    '''
    Stores list of busy/available workers
    '''

    def __init__(self, workers):
        self.workers = workers
        self.availableWorkers = workers
        self.busyWorkers = []

    def areAvailable(self):
        return any([worker.isAvailable for worker in self.availableWorkers])

    def getAvailable(self):
        return self.availableWorkers.pop()

    def moveToBusy(self, worker):
        self.busyWorkers.append(worker)

    def secondsTick(self):
        nodesToremove = []
        print(f'second ticked: workers: {self.workers}, free: {self.availableWorkers}, busy: {self.busyWorkers}')
        for worker in self.busyWorkers:
            worker.secondsTick()

        for worker in self.busyWorkers:
            if worker.isAvailable():
                print(f'worker: {worker}, with letter {worker.workLetter} became available, returning to free pool')
                self.availableWorkers.append(worker)
                self.busyWorkers.remove(worker)

                nodesToremove.append(worker.workLetter)

        return nodesToremove


class Worker():
    def __init__(self):
        self.stepDuration = {item[0]: item[1] for item in zip(
            list(string.ascii_uppercase), range(61, 88))}
        self.workSecondsLeft = 0
        self.workLetter = ''

    def isAvailable(self):
        if self.workSecondsLeft == 0:
            return True
        else:
            return False

    def assignWork(self, letter):
        self.workLetter = letter
        self.workSecondsLeft = self.stepDuration[letter]
        print(f'set work duration to {self.workSecondsLeft} and work letter to {letter}')

    def secondsTick(self):
        self.workSecondsLeft -= 1


steps = ''
graph = buildGraph(input)
seconds = 0
workerPool = Pool([Worker() for i in range(5)])
blocked = []


while graph:
    while workerPool:
        print(f'blocked nodes: {blocked}, seconds: {seconds}')
        seconds += 1
        if graph:
            print(f'current graph.indegree: {graph.in_degree}')
            next_steps = [n for n, d in graph.in_degree if d == 0]

            for step in next_steps:
                if step not in blocked:
                    if workerPool.areAvailable():
                        worker = workerPool.getAvailable()
                        print(f'assigning {step} to {worker}')
                        worker.assignWork(step)
                        blocked.append(step)
                        workerPool.moveToBusy(worker)
        nodesToremove = workerPool.secondsTick()
        if nodesToremove:
            for node in nodesToremove:
                print(f'removing {node} item')
                graph.remove_node(node)
                steps += node
                nodesToremove = []
        if not graph:
            break

print(steps)
print(seconds)
