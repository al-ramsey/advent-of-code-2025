from aoc_useful_functions import *
import copy # python is so stupid sometimes. yes, when I say copy, I do indeed want a copy -_-

file = r"[PATH]"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()

lines = [l[:-1] for l in lines]
lines = [l.split(",") for l in lines]
lines = [[int(el) for el in l] for l in lines]

def part1(lines):

    areas = []
    for i in range(len(lines)):
        areal = []
        for j in range(len(lines)):
            areal.append(product([lines[i][0]-lines[j][0]+1, lines[i][1] - lines[j][1]+1]))
        areas.append(areal)

    return max(flatten(areas))

def abs(i):
    if i < 0:
        return -1*i
    else:
        return i

def picture(lines):
    grid = []
    maxx = max([l[0] for l in lines])
    maxy = max([l[1] for l in lines])
    greens = []
    for i in range(len(lines)):
        if lines[i][0] == lines[(i+1) % len(lines)][0]:
            #print(lines[i], lines[(i+1) % len(lines)])
            if lines[i][1] < lines[(i+1)%len(lines)][1]:
                greens += [[lines[i][0], lines[i][1]+j] for j in range(1, abs(lines[i][1] - lines[(i+1) % len(lines)][1]))]
            else:
                greens += [[lines[i][0], lines[i][1]-j] for j in range(1, abs(lines[i][1] - lines[(i+1) % len(lines)][1]))]
        
        if lines[i][1] == lines[(i+1) % len(lines)][1]:
            if lines[i][0] < lines[(i+1)%len(lines)][0]:
                greens += [[lines[i][0]+j, lines[i][1]] for j in range(1, abs(lines[i][0] - lines[(i+1) % len(lines)][0]))]
            else:
                greens += [[lines[i][0]-j, lines[i][1]] for j in range(1, abs(lines[i][0] - lines[(i+1) % len(lines)][0]))]

    for i in range(maxx+2):
        gridl = []
        for j in range(maxy+2):
            if [i,j] in lines:
                gridl.append(2)
            elif [i,j] in greens:
                gridl.append(1)
            else:
                gridl.append(0)
        
        grid.append(gridl)
    
    grid = flip(grid)
        
    return grid

def component(l, lines, el):
    # find the connected component of `l` which the element `el` is contained in
    # this function is an old one from one of the 2024 days
    # it's also a bottleneck, so probably wildly inefficient
    surr = surroundings(el, lines)
    surr = [s for s in surr if s in l]
    old_track = [[el]]
    new_track = [[el], surr.copy()]

    while len(set(flatten(new_track))) > len(set(flatten(old_track))):
        new_end = []
        for coord in new_track[-1]:
            if coord not in set(flatten(old_track)):
                surr = surroundings(coord, lines)
                surr = [s for s in surr if s in l]
                new_end += surr.copy()

        new_end = list(set(new_end))
        old_track = new_track.copy()
        new_track.append(new_end)

    return list(set(flatten(new_track)))

def compress(lines):
    # I believe this is called coordinate compression
    # courtesy of someone on reddit suggesting it
    xs = sorted(list(set([l[0] for l in lines])))
    ys = sorted(list(set([l[1] for l in lines])))
    xd = {}
    yd = {}
    for i in range(len(xs)):
        dict_adder(xd, xs[i], i+1)
    for i in range(len(ys)):
        dict_adder(yd, ys[i], i+1)

    new_lines = [[xd[l[0]], yd[l[1]]] for l in lines]
    return new_lines, xd, yd

def part2(lines):

    li, xd, yd = compress(lines)
    grid = picture(li)

    l = find(0, grid)
    comp = component(l, grid, (0,0))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in comp and grid[i][j] == 0:
                grid[i][j] = 3

    areas = []
    for i in range(len(li)):
        for j in range(len(li)):
            insq = [(k1, k2) for k1 in range(min(li[i][0], li[j][0]), max(li[i][0], li[j][0])+1) for k2 in range(min(li[i][1], li[j][1]), max(li[i][1], li[j][1])+1)]
            broken = False
            for coord in insq:
                if grid[coord[1]][coord[0]] == 0:
                    broken = True
                    break

            if not broken:
                ix = list(xd.keys())[list(xd.values()).index(li[i][0])]
                iy = list(yd.keys())[list(yd.values()).index(li[i][1])]
                jx = list(xd.keys())[list(xd.values()).index(li[j][0])]
                jy = list(yd.keys())[list(yd.values()).index(li[j][1])]
                areas.append(product([abs(ix-jx)+1, abs(iy-jy)+1]))

    return max(areas)

#print(part2(lines))
# my answer: 1603439684