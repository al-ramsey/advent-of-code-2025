#file = r"[PATH]"
#filein = open(file, "r", encoding='UTF-8')
#lines = filein.readlines()
#filein.close()
# remove \n
#lines = [line[:-1] for line in lines]

def part1(lines):

    count = 0

    for line in lines:
        ints = [line[i] for i in range(len(line))]
        ints = [int(i) for i in ints]
        # pick the highest number that isn't the last digit
        s = str(max(ints[:-1]))
        sind = ints.index(int(s))
        # pick the highest number appearing after the first number 
        e = str(max(ints[sind+1:]))
        count += int(s+e)

    return count

def part2(lines):

    count = 0

    for line in lines:
        ints = [int(line[i]) for i in range(len(line))]
        # pick the highest number that would be possible to begin with
        s = str(max(ints[:-11]))
        sind = ints.index(int(s))
        string = s
        while(len(string)) < 12:
            if len(string) == 11:
                # (no upper index limit)
                e = str(max(ints[sind+1:]))
                string += e
                break

            e = str(max(ints[sind+1:-11+len(string)]))
            sind = ints[sind+1:-11+len(string)].index(int(e)) + sind + 1
            string += e

        count += int(string)
    
    return count

#print(part2(lines))