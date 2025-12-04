#file = r"[PATH]"
#filein = open(file, "r", encoding='UTF-8')
#lines = filein.readlines()
#filein.close()
# remove \n
#lines = [line[:-1] for line in lines]

def diag_surroundings(en : list, lines):
    # find all adjacent positions
    i = en[0]
    j = en[1]
    left = (i, j-1)
    right = (i, j+1)
    up = (i+1, j)
    down = (i-1, j)
    dl = (i-1, j-1)
    dr = (i-1, j+1)
    ul = (i+1, j-1)
    ur = (i+1, j+1)
    cs = [left, right, up, down, dl, dr, ul, ur]
    cs = [c for c in cs if (c[0] >= 0 and c[0] < len(lines) and c[1] >= 0 and c[1] < len(lines))]

    return cs

def mark_reached(lines):
    # find all positions with paper which can be reached

    reached = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "@":
                surr = diag_surroundings((i,j), lines)
                c = [s for s in surr if lines[s[0]][s[1]] == "@"]
                if len(c) < 4:
                    reached.append((i,j))

    # remove duplicates
    reached = list(set(reached))
    return reached

def part1(lines):
    return len(mark_reached(lines))

#print(part1(lines))

def remove_reached(lines, remove):
    # remove any paper which can be reached
    newlines = []
    for i in range(len(lines)):
        newline = []
        for j in range(len(lines[0])):
            if (i,j) in remove:
                newline += "."
            else:
                newline += lines[i][j]
        newlines.append(newline)
    
    return newlines

def part2(lines):
    loop = True
    count = 0
    while loop:
        remove = mark_reached(lines)
        # if we can't remove any more, break the loop
        if len(remove) == 0:
            loop = False
        count += len(remove)
        lines = remove_reached(lines, remove)
    
    return count

#print(part2(lines))
