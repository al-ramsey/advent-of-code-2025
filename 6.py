from aoc_useful_functions import *

file = r"[PATH]"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()
# remove \n
lines = [l[:-1] for l in lines]

def find_operations(s):
    # s string, return list of operations in it
    ops = ['*', '+']
    l = [el for el in s if el in ops]
    return l

def part1(lines):
    nums = lines[:-1]
    operations = lines[-1]
    # remove spaces
    nums = [find_ints(el) for el in nums]
    operations = find_operations(operations)
    cleaned_input = nums + [operations]

    problems = flip(cleaned_input)
    tot = 0
    for p in problems:
        if p[-1] == "+":
            tot += sum(p[:-1])
        else:
            tot += product(p[:-1])

    return tot

#print(part1(lines))

def helper(ns):
    # take in something like [[1], [12], [34], [], [1], [123], [], ...]
    # return [[1, 12], [34], [1, 123], ...]
    indices = all_occ(ns, [])
    new = [ns[:indices[0]]] + flatten([[ns[indices[j]+1:indices[j+1]] for j in range(len(indices)-1)]]) + [ns[indices[-1]+1:]]
    new = [flatten(el) for el in new]
    return new

def part2(lines):

    operations = find_operations(lines[-1])
    f = flip(lines[:-1])

    ns = [find_ints_in_list(el) for el in f]
    ns = helper(ns)

    tot = 0
    for k in range(len(operations)):
        if operations[k] == "+":
            tot += sum(ns[k])
        else:
            tot += product(ns[k])

    return tot

#print(part2(lines))