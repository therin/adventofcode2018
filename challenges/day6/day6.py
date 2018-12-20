# -*- coding: utf-8 -*-
from collections import defaultdict

points = []

def main():
    with open("input.txt", "r") as input:
        for line in input.readlines():
            a,b = line.strip().split(", ")
            points.append((int(a), int(b)))
    finite_regions = [p for p in points if  in_finite_region(p)]
    finite_areas = [area(p) for p in finite_regions]
    print("1: " + str(max(finite_areas)))

    answer = area_less_than(10000)
    print("2: " + str(answer))

def taxicab(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#Test that a region is bounded if you continue to move in a direction
def bounded_direction(point, direction):
    distances_from_points = [taxicab(p, point) for p in points]
    delta_point = (point[0], point[1])

    #If the delta_point moves outside the region, then the original region is bounded in this directioon
    while in_region(delta_point) == point:
        delta_point = (delta_point[0] + direction[0], delta_point[1] + direction[1])
        distances_from_delta = [taxicab(p, delta_point) for p in points]

        #Check if distances from all points grew; if it did, region is unbounded
        grew = [distances_from_points[i] + 1 == distances_from_delta[i] for i in range(len(points))]
        if all(grew):
            return False

        #Didn't all grow; save old distances for later comparison
        distances_from_points = distances_from_delta[:]
        
    return True

#A finite region will be bounded from all directions
def in_finite_region(p):
    return all(bounded_direction(p, d) for d in [(0,1), (0, -1), (1, 0), (-1, 0)])

#A point is in a region if there is only one point that
#is closest to it
def in_region(p):
    min_distance = min(taxicab(p,point) for point in points)
    closest = [point for point in points if taxicab(p,point) == min_distance]
    if len(closest) == 1:
        return closest[0]
    else:
        return False

def area(p):
    region_points = set([p])
    neigh = neighbors(p)
    while len(neigh) != 0:
        next_p = neigh.pop()
        if in_region(next_p) == p:
            region_points.add(next_p)
            neigh.extend([n for n in neighbors(next_p) if n not in region_points])
    return len(region_points)

def area_less_than(n):
    region_points = set()

    #Pick a random starting point
    point = points[0]
    neigh = neighbors(point)
    while len(neigh) != 0:
        next_point = neigh.pop()
        if less_than(n, next_point):
            region_points.add(next_point)
            neigh.extend([n for n in neighbors(next_point) if n not in region_points])
    return len(region_points)

def less_than(n, p):
    return sum(taxicab(p, point) for point in points) < n
            
def neighbors(point):
    neigh = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            neigh.append((point[0] + i, point[1] + j))
    neigh.remove(point)
    return neigh

if __name__ == "__main__":
    main()
