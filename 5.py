file = r"[PATH]"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()
lines = [l[:-1] for l in lines]

i = lines.index('')
ranges = lines[:i]
ids = lines[i+1:]

ranges = [r.split("-") for r in ranges]
ranges = [[int(r) for r in rs] for rs in ranges]

def part1(ranges, ids):
    count = 0
    for j in ids:
        for r in ranges:
            if int(j) >= int(r[0]) and int(j) <= int(r[1]):
                count += 1
                break
    
    return count

#print(part1(ranges, ids))

#upper_bounds = max([int(r[1]) for r in ranges])

# was worth a try, but gives a memory error
#ids = [k for k in range(upper_bounds+1)]

#print(part1(ranges, ids))

def part2(ranges):

    count = 0
    k = min(r[0] for r in ranges)
    m = max(r[1] for r in ranges)

    while k < m:

        broken = False
        for r in ranges:
            # if k is in range, add to the count until you get to the upper bound then set k to be one more than it
            if k >= r[0] and k <= r[1]:
                count += r[1] - k + 1
                k = r[1] + 1
                broken = True
                break
        
        # if k wasn't in any range, set it to be the minimum next lower bound
        if not broken:
            valid_mins = [r[0] for r in ranges if r[0] >= k]
            vmin = min(valid_mins)
            k = vmin

    return count

#print(part2(ranges))

# 355811683010841 is too low
# 381559290800531 is too high
# 360341832208407 is just right :-)