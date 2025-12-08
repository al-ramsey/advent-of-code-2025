from aoc_useful_functions import flatten
import math
#import time

file = r"[PATH]"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()

lines = [l[:-1] for l in lines]
lines = [l.split(",") for l in lines]
lines = [[int(k) for k in l] for l in lines]

def dist(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2] - y[2])**2)

def dist_array(lines):
    d = []
    for i in range(len(lines)):
        dline = []
        for j in range(len(lines)):
            dline.append(dist(lines[i], lines[j]))
        d.append(dline)
    
    return d

connections = [[0]*i +[1] + [0]*(len(lines)-i-1) for i in range(len(lines))]
connections = connections.copy()

def connect_these(connections, d):
    newl = connections[d[1]]
    newl = newl[:d[2]] + [1] + newl[d[2]+1:]
    connections = connections[:d[1]] + [newl] + connections[d[1]+1:]

    return connections

def connected_components(connections):
    ccoords = []
    for i in range(len(connections)):
        for j in range(len(connections)):
            if j > i and connections[i][j] == 1:
                ccoords.append([i,j])

    while len(flatten(ccoords)) > len(set(flatten(ccoords))):
        new_ccoords = []
        broken = False
        for i in range(len(ccoords)):
            for j in range(len(ccoords)):
                if i != j:
                    if set(ccoords[i]).intersection(set(ccoords[j])) != set():
                        #print({} == set()) # apparently {} is not the empty set??
                        new_ccoords.append(list(set(ccoords[i]).union(set(ccoords[j]))))
                        broken = True
                        break
            
            if broken:
                break
        
        x = ccoords[i]
        y = ccoords[j]
        ccoords.remove(x)
        ccoords.remove(y)
        ccoords = new_ccoords + ccoords
    
    co = [len(c) for c in ccoords]
    cop = [1]*(len(connections)-sum(co))
    return co + cop

def part1(lines, connections, r):

    darray = dist_array(lines)
    darray_sorted = sorted(list(set(flatten(darray))))[1:] # I HATE SETS SO MUCH!!!!!!!!!! (I originally wrote list(set(sorted(...))) :)))))))))) )
    flat_darray = flatten(darray)

    for i in range(r):
        d0 = darray_sorted[i]
        d12 = flat_darray.index(d0)
        d2 = (d12 % len(lines)) 
        d1 = math.floor(d12/len(lines))
        d = (d0, d1, d2)

        connections = connect_these(connections, d)

    c = connected_components(connections)
    c = sorted(c)
    #print(lines[d1][0]*lines[d2][0]) # uncomment when you find r for part 2

    p = 1
    for i in range(3): # change to 2 for part 2
        p*= c[-(i+1)]

    #print(len(c)) # uncomment when finding r on part 2

    return p

#print(part1(lines, connections, 1000))
'''
method for day 2: the part commented out with the docstring comments below was taking way too long to run, so
here's the method I used: change range(3) to range(2) in part1, then run it for r taking values from
1000-10000. For me, by the time of 10000 iterations, all components were connected, so you get an index error.
Every time you get an index error, pick your new value of r halfway between the lowest value with an index
error and the highest value without one; after a few tries, you get to the first value of r that raises the error. 
Now, uncomment out the line that prints lines[d1][0]*lines[d2][0] - this is the answer.

This is sort of cheating, but it's late, and it worked. On my input r = 3778.
'''
#print(part1(lines, connections, 3778))

'''
what's below doesn't work (too slow), but I'm leaving it in for historical interest

darray = dist_array(lines)
darray_sorted = sorted(list(set(flatten(darray))))[1:]
flat_darray = flatten(darray)

c = connected_components(connections)
i = 0
while len(c) > 1:
    d0 = darray_sorted[i]
    d12 = flat_darray.index(d0)
    d2 = (d12 % len(lines)) 
    d1 = math.floor(d12/len(lines))
    d = (d0, d1, d2)

    connections = connect_these(connections, d)
    c = connected_components(connections)
    if len(c) == 1:
        print(lines[d1], lines[d2])
        print(lines[d1][0]*lines[d2][0])
    i += 1
'''