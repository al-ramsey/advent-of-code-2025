from aoc_useful_functions import dict_adder

file = r"[PATH]"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()
lines = [l[:-1] for l in lines]
lines = [list(l) for l in lines]

def part1(lines):

    count = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i-1][j] == "S":
                lines[i][j] = "|"

            if lines[i][j] == "^":
                if lines[i-1][j] == "|":
                    lines[i][j-1] = "|"
                    lines[i][j+1] = "|"
                    # it split, so add one to the count
                    count += 1

            elif lines[i-1][j] == "|":
                lines[i][j] = "|"

    return count

def part2(lines):

    start = (1, lines[0].index("S"))
    # make a dictionary whose elements are points in lines[i]
    # and whose values are the number of paths ending at that point
    paths = {start:1}
    i = 1

    while i < len(lines) - 1:
        i += 1
        new_paths = {}
        for path in paths:
            split = False

            if lines[i][path[1]] == "^":
                dict_adder(new_paths, (i, path[1]-1), paths[path])
                dict_adder(new_paths, (i, path[1]+1), paths[path])
                split = True

            if not split:
                dict_adder(new_paths, (i, path[1]), paths[path])
        
        paths = new_paths
                
    count = 0
    for p in paths:
        count += paths[p]

    return count

#print(part1(lines))
#print(part2(lines))
