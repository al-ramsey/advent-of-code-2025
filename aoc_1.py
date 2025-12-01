#file = r"[PATH]"
#filein = open(file, "r", encoding='UTF-8')
#lines = filein.readlines()
#filein.close()

def part1(lines):
    val = 50
    counter = 0

    for line in lines:
        if line[0] == "L":
            val -= int(line[1:-1])
        else:
            val += int(line[1:-1])

        val = val % 100
        if val == 0:
            counter += 1

    return counter

#print(part1(lines))

def part2(lines):
    val = 50
    counter = 0
    for line in lines:
        old_val = val
        if line[0] == "L":
            val -= int(line[1:-1])
        else:
            val += int(line[1:-1])
        
        if val == 0:
            counter += 1

        else:
            while val < 0:
                val += 100
                counter += 1
                # reverses double counting past zero
                if val >= 0 and old_val == 0:
                    counter -= 1
                # recounts if ending on zero
                if val == 0:
                    counter += 1
            while val > 99:
                val -= 100
                counter += 1
    
    return counter

#print(part2(lines))